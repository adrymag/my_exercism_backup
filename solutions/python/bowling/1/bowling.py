"""
Bowling — Exercism Python Track

A bowling score calculator that tracks rolls frame-by-frame and computes
the total score at the end of the game.

Scoring rules
-------------
• 10 frames per game.
• Open frame: fewer than 10 pins in 2 rolls → score = pins knocked down.
• Spare: all 10 pins in 2 rolls → score = 10 + next roll.
• Strike: all 10 pins in 1 roll → score = 10 + next 2 rolls.
• 10th frame special case:
    – Strike on roll 1 → 2 fill balls (to compute the strike bonus).
    – Spare on rolls 1+2 → 1 fill ball.
    – Open frame → no fill balls, game ends.
    – Fill balls themselves do not generate more fill balls.

Error handling
--------------
• IndexError("cannot throw bonus with an open tenth frame")
    – thrown when a roll is attempted after an open 10th frame.
• ValueError("invalid fill balls")
    – thrown for invalid pin counts, too many pins in a frame,
      or rolling after the game is already complete.
"""


class BowlingGame:
    """Track rolls for a single game of bowling and compute the final score."""

    def __init__(self):
        """Initialise a fresh game.

        State machine variables:
            rolls          — list of every valid roll (pin count).
            frame          — current frame number (1–10).
            roll_in_frame  — 1st, 2nd, or 3rd roll within the current frame.
            pins_up        — pins still standing before the current roll.
            fill_balls     — how many fill balls remain in the 10th frame.
            game_over      — True once the 10th frame is fully resolved.
            tenth_open     — True if the 10th frame ended open (no strike/spare).
        """
        self.rolls = []
        self.frame = 1
        self.roll_in_frame = 1
        self.pins_up = 10
        self.fill_balls = 0
        self.game_over = False
        self.tenth_open = False

    def roll(self, pins):
        """Record a single roll.

        Args:
            pins (int): Number of pins knocked down (0–10).

        Raises:
            IndexError: If a bonus roll is attempted after an open 10th frame.
            ValueError: If the pin count is invalid or the game is already
                        finished.
        """
        # -------------------------------------------------------------------
        # Guard: no rolls allowed once the game is finished.
        # -------------------------------------------------------------------
        if self.game_over:
            if self.tenth_open:
                raise IndexError("cannot throw bonus with an open tenth frame")
            raise ValueError("invalid fill balls")

        # -------------------------------------------------------------------
        # Validate the raw pin count.
        # -------------------------------------------------------------------
        if pins < 0 or pins > 10:
            raise ValueError("invalid fill balls")

        # -------------------------------------------------------------------
        # Validate against the pins actually standing in the current frame.
        # -------------------------------------------------------------------
        if pins > self.pins_up:
            raise ValueError("invalid fill balls")

        # Record the roll.
        self.rolls.append(pins)

        # -------------------------------------------------------------------
        # Update game state based on which frame we are in.
        # -------------------------------------------------------------------
        if self.frame < 10:
            self._handle_normal_frame(pins)
        else:
            self._handle_tenth_frame(pins)

    def _handle_normal_frame(self, pins):
        """Transition state for frames 1 through 9.

        Frame 1–9 logic:
            • Roll 1: if strike (10 pins), the frame ends immediately and we
              advance to the next frame with a fresh set of 10 pins.
            • Roll 1 (not strike): remember how many pins are left, move to
              roll 2.
            • Roll 2: the frame always ends; advance to the next frame.
        """
        if self.roll_in_frame == 1:
            if pins == 10:
                # Strike — frame complete in one roll.
                self.frame += 1
                # pins_up stays 10 for the next frame.
            else:
                # Not a strike — prepare for the second roll.
                self.pins_up = 10 - pins
                self.roll_in_frame = 2
        else:
            # Second roll — frame complete regardless of outcome.
            self.frame += 1
            self.roll_in_frame = 1
            self.pins_up = 10

    def _handle_tenth_frame(self, pins):
        """Transition state for the special 10th frame.

        10th-frame logic:
            • Roll 1:
                – Strike → 2 fill balls awarded, fresh 10 pins, go to roll 2.
                – Otherwise → subtract pins, go to roll 2.
            • Roll 2:
                – If we are in fill-ball mode (after a strike on roll 1):
                    * Strike again → fresh 10 pins for roll 3.
                    * Otherwise → 10 - pins remain for roll 3.
                    In both cases we advance to roll 3.
                – If no strike on roll 1:
                    * Spare (pins == pins_up) → 1 fill ball, fresh 10 pins,
                      go to roll 3.
                    * Open (pins < pins_up) → game over, no fill balls.
            • Roll 3 (fill ball):
                – Always ends the game.
        """
        if self.roll_in_frame == 1:
            if pins == 10:
                # Strike in the 10th — two fill balls coming.
                self.fill_balls = 2
                self.pins_up = 10
                self.roll_in_frame = 2
            else:
                self.pins_up = 10 - pins
                self.roll_in_frame = 2

        elif self.roll_in_frame == 2:
            if self.fill_balls > 0:
                # We are processing a fill ball after a strike on roll 1.
                self.fill_balls -= 1
                if pins == 10:
                    self.pins_up = 10
                else:
                    self.pins_up = 10 - pins
                self.roll_in_frame = 3
            else:
                # No strike on roll 1 — check for spare or open.
                if pins == self.pins_up:
                    # Spare — one fill ball.
                    self.fill_balls = 1
                    self.pins_up = 10
                    self.roll_in_frame = 3
                else:
                    # Open frame — game ends immediately.
                    self.tenth_open = True
                    self.game_over = True

        else:
            # Roll 3 is always the final roll of the game.
            self.game_over = True

    def score(self):
        """Compute and return the total score for the completed game.

        The algorithm walks through the 10 frames using a single index
        into the `rolls` list.

            • Strike  → add 10 + next two rolls, advance index by 1.
            • Spare   → add 10 + next roll, advance index by 2.
            • Open    → add the two rolls, advance index by 2.

        This works for the 10th frame as well because any fill balls are
        already present in `rolls` immediately after the 10th-frame rolls.

        Returns:
            int: Total score (0–300).
        """
        total = 0
        roll_idx = 0

        for _ in range(10):
            first = self.rolls[roll_idx]

            if first == 10:
                # Strike: bonus = next two rolls.
                total += 10 + self.rolls[roll_idx + 1] + self.rolls[roll_idx + 2]
                roll_idx += 1
            elif first + self.rolls[roll_idx + 1] == 10:
                # Spare: bonus = next roll.
                total += 10 + self.rolls[roll_idx + 2]
                roll_idx += 2
            else:
                # Open frame.
                total += first + self.rolls[roll_idx + 1]
                roll_idx += 2

        return total