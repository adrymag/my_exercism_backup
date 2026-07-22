def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    divisors_sum = 1
    current_divisor = 2
    tested = False
    
    while current_divisor * current_divisor <= number :
        if number % current_divisor == 0:
            if current_divisor * current_divisor < number:
                divisors_sum = divisors_sum + current_divisor + number / current_divisor
            else:
                divisors_sum = divisors_sum + current_divisor
        if divisors_sum > number:
            return "abundant"
        current_divisor = current_divisor + 1
        tested = True
        
    if tested and divisors_sum == number:
        return "perfect"
    
    return "deficient"