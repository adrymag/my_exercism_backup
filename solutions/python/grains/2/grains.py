def square(number):
    """
    This particular exercise requires that you use the raise statement to "throw" a ValueError when the square
    input is out of range. The tests will only pass if you both raise the exception and include a message with it.
    
    To raise a ValueError with a message, write the message as an argument to the exception type:
    
    # when the square value is not in the acceptable range        
    raise ValueError("square must be between 1 and 64")
    """
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")      

def total():
    return 2 ** 64 - 1