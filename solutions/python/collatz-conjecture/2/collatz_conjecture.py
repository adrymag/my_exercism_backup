def steps(number):
    """Determine the number of steps required to reach 1 following the rules of the Collatz Conjecture
    Parameters:
        number (int): a positive integer.

    Returns:
        int: The number of steps rquired to reach 1 starting from the input number and following the rules of the Collatz Conjecture.
    """
    
    # example when argument is zero or a negative integer
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        # return -1
    
    steps_count = 0

    while number != 1:
        steps_count = steps_count + 1
        
        if number % 2 == 0 :
            number = number / 2
        else :
            number = 3 * number + 1
          
    return steps_count