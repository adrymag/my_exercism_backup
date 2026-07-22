def square(number):
    """
    Parameters:
        number (int): The number of the current chess board square.

    Returns:
        int: The number of grains on the square # number from the chess board.
    
    This particular exercise requires that you use the raise statement to "throw" a ValueError when the square
    input is out of range. The tests will only pass if you both raise the exception and include a message with it.
    
    To raise a ValueError with a message, write the message as an argument to the exception type:
    
    # when the square value is not in the acceptable range        
    raise ValueError("square must be between 1 and 64")
    """
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")      

def total():
    """
    Returns:
        int: The total number of grains on the chess board.
    """
    return 2 ** 64 - 1