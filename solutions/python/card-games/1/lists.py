"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2  # rounds_1.append(rounds_2)


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    start_end_average = ( hand[0] + hand[-1] ) / 2

    if start_end_average == card_average(hand):
        return True

    # hand.sorted = sort(hand)
    hand.sort()
    
    mid_card_average = hand[ int( ( len(hand) - 1 ) / 2 ) ] # median_average = 
    
    return mid_card_average == card_average(hand)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    # average_even = sum([hand[hand_counter] for hand_counter in range(len(hand))] if hand_counter % 2 = 0]) / count([hand[hand_counter] for hand_counter in range(len(hand))] if hand_counter % 2 = 0])

    average_even = sum([h for i, h in enumerate(hand) if i % 2 == 0]) / sum([1 for i, h in enumerate(hand) if i % 2 == 0])
    # average_even = sum( [hand[hand_counter] for hand_counter in 0..len(hand) where hand_counter % 2 = 0] ) / sum( [1 for hand_counter in 0..len(hand) where hand_counter % 2 = 0] )
    average_odd = sum([h for i, h in enumerate(hand) if i % 2 == 1]) / sum([1 for i, h in enumerate(hand) if i % 2 == 1])
    # average_odd = sum( [hand[hand_counter] for hand_counter in 0..len(hand) where hand_counter % 2 = 1] ) / sum( [1 for hand_counter in 0..len(hand) where hand_counter % 2 = 1] )

    return average_even == average_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    

    return hand[:-1] + [ 2 * hand[-1] if hand[-1] == 11 else hand[-1]]
