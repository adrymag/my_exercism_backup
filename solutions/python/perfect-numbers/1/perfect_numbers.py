def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    s = 1
    d = 2
    tested = False
    
    while d * d <= number :
        if number % d == 0:
            if d * d < number:
                s = s + d + number / d
            else:
                s = s + d
        if s > number:
            return "abundant"
        d = d + 1
        tested = True
        
    if tested and s == number:
        return "perfect"
    else:
        return "deficient"