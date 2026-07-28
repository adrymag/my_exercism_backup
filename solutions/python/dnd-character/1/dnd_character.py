"""Dungeons & Dragons character generator.

Simulates rolling four 6-sided dice for each of the six character abilities,
dropping the lowest die, and summing the remaining three. Hitpoints are
calculated from the constitution modifier.
"""

import random


def modifier(value):
    """Calculate a D&D ability modifier from an ability score.

    The formula is: subtract 10 from the score, divide by 2, and round down.
    In Python, floor division (//) handles the "round down" requirement
    for both positive and negative numbers.

    Parameters:
        value (int): The ability score (e.g., constitution).

    Returns:
        int: The ability modifier.
    """
    return (value - 10) // 2


class Character:
    """Represents a D&D player character with six abilities and hitpoints."""

    def __init__(self):
        """Generate a new character with randomized ability scores.

        For each of the six abilities, we simulate rolling four 6-sided dice,
        discarding the lowest roll, and summing the highest three. The
        character's hitpoints are then set to 10 plus the constitution modifier.
        """
        # Roll ability scores for each of the six core D&D abilities.
        # The public ability() method is reused here to ensure consistency.
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        # Hitpoints start at 10 plus the constitution modifier.
        # The modifier function encapsulates the (score - 10) // 2 formula.
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Simulate rolling 4d6 and return the sum of the highest three dice.

        This public method can be called on a Character instance to generate
        a single ability score. It is also used internally during __init__.

        Returns:
            int: The generated ability score (always between 3 and 18).
        """
        # Roll four 6-sided dice. random.randint(1, 6) gives an inclusive
        # range matching a standard die face.
        rolls = [random.randint(1, 6) for _ in range(4)]

        # Sort the rolls in ascending order so the lowest value is first.
        rolls.sort()

        # Discard the lowest roll (index 0) and sum the remaining three.
        # Slicing [1:] gives the three highest values.
        return sum(rolls[1:])