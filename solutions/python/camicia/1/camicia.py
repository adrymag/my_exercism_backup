"""
Camicia — Exercism Python Track

Simulate a two-player card game similar to the classic "Camicia" (also known
as "Egyptian Ratscrew" or "War" in some cultures).

Rules summary
-------------
• Two players take turns playing the top card of their deck onto a central
  pile.
• Number cards (2–10): play passes to the other player.
• Payment cards (J=1, Q=2, K=3, A=4): the opponent must pay that many cards.
• If a player reveals a payment card while paying a penalty, they stop
  paying; the other player must now pay the new penalty.
• If a penalty is fully paid without interruption, the player who played the
  last payment card collects the pile.
• If a player cannot play (deck empty), the other player collects the pile.
• If one player holds every card after a collection, the game ends.
• A loop is detected when a round-start state (decks + starter) repeats,
  ignoring the specific values of number cards.

Return value
------------
A dict with keys:
    status  — "finished" or "loop"
    cards   — total cards played onto the central pile
    tricks  — number of times the pile was collected
"""

from collections import deque


# ---------------------------------------------------------------------------
# Payment card mapping: card name → penalty (number of cards opponent must
# play).
# ---------------------------------------------------------------------------
PAYMENT = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}


def normalize_card(card):
    """Return a canonical representation of a card for loop detection.

    Payment cards (J, Q, K, A) keep their identity.  Everything else is
    treated as a generic number card ('N').  This implements the rule
    "not counting number cards" when checking for repeated game states.
    """
    s = str(card).upper()
    return s if s in PAYMENT else 'N'


def simulate_game(player_a, player_b):
    """Simulate the Camicia card game.

    Args:
        player_a (list): Player A's deck.  Leftmost element is the top card.
        player_b (list): Player B's deck.  Leftmost element is the top card.

    Returns:
        dict: {"status": "finished" | "loop",
               "cards":  int,   # total cards placed on the pile
               "tricks": int}   # number of collections
    """

    # -----------------------------------------------------------------------
    # Use deques so that popping from the front (top of deck) and appending
    # to the back (bottom of deck) are both O(1) operations.
    # -----------------------------------------------------------------------
    a = deque(player_a)
    b = deque(player_b)

    total_cards = 0   # cards placed on the central pile across all rounds
    tricks = 0        # how many times the pile has been collected
    starter = 'A'     # which player begins the next round

    # -----------------------------------------------------------------------
    # Loop detection: every round-start state is recorded.
    #
    # A state is a 3-tuple: (normalized_A, normalized_B, starter).
    # Normalization replaces every number card with the sentinel 'N',
    # so only the positions of payment cards matter.
    #
    # If we ever encounter a state we have seen before, the game has
    # entered an infinite loop.
    # -----------------------------------------------------------------------
    seen_states = set()

    while True:
        # ---------------------------------------------------------------
        # 1. Loop detection at the start of the round.
        # ---------------------------------------------------------------
        norm_a = tuple(normalize_card(c) for c in a)
        norm_b = tuple(normalize_card(c) for c in b)
        state = (norm_a, norm_b, starter)

        if state in seen_states:
            return {"status": "loop", "cards": total_cards, "tricks": tricks}
        seen_states.add(state)

        # ---------------------------------------------------------------
        # 2. Play one complete round.
        #
        # A round is a sequence of card plays that ends when someone
        # collects the central pile.  Collection occurs in two ways:
        #   a) A penalty is fully paid → the last payment-card player
        #      collects.
        #   b) A player cannot play (empty deck) → the other player
        #      collects.
        #
        # Variables inside the round:
        #   active    — whose turn it is to play ('A' or 'B').
        #   penalty   — how many cards the active player must still pay.
        #               0 means it is a normal turn, not a penalty.
        #   collector — who played the last payment card.  They collect if
        #               the current penalty is completed without another
        #               payment card appearing.
        # ---------------------------------------------------------------
        pile = []         # cards played during this round
        active = starter  # whose turn it is
        penalty = 0       # cards remaining to pay (0 = normal turn)
        collector = None  # player who would collect on clean penalty end

        while True:
            deck = a if active == 'A' else b

            # -----------------------------------------------------------
            # Case A: active player has no cards.
            # The other player collects the pile immediately.
            # -----------------------------------------------------------
            if len(deck) == 0:
                other = 'B' if active == 'A' else 'A'
                other_deck = b if other == 'B' else a
                other_deck.extend(pile)

                tricks += 1
                total_cards += len(pile)

                # If one player now holds every card, the game is over.
                if len(a) == 0 or len(b) == 0:
                    return {"status": "finished",
                            "cards": total_cards,
                            "tricks": tricks}

                # The collector starts the next round.
                starter = other
                break

            # -----------------------------------------------------------
            # Case B: active player plays their top card.
            # -----------------------------------------------------------
            card = deck.popleft()
            pile.append(card)

            if penalty > 0:
                # We are currently paying a penalty.
                penalty -= 1

                if str(card).upper() in PAYMENT:
                    # A payment card appeared while paying!
                    # The current player stops; the other player must now
                    # pay the new penalty.  The current player becomes the
                    # collector for this new penalty.
                    collector = active
                    penalty = PAYMENT[str(card).upper()]
                    active = 'B' if active == 'A' else 'A'

                elif penalty == 0:
                    # The penalty was fully paid with no interruption.
                    # The player who set this penalty collects.
                    collector_deck = a if collector == 'A' else b
                    collector_deck.extend(pile)

                    tricks += 1
                    total_cards += len(pile)

                    if len(a) == 0 or len(b) == 0:
                        return {"status": "finished",
                                "cards": total_cards,
                                "tricks": tricks}

                    starter = collector
                    break
                # If penalty is still > 0, the same player continues.

            else:
                # Normal turn (no active penalty).
                if str(card).upper() in PAYMENT:
                    # Payment card: opponent must pay the penalty.
                    collector = active
                    penalty = PAYMENT[str(card).upper()]
                    active = 'B' if active == 'A' else 'A'
                else:
                    # Number card: simply pass the turn.
                    active = 'B' if active == 'A' else 'A'