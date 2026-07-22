def convert(number):
    """If a given number:

    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.
    """
    s = ""
    # is_divisible = False
    
    if number % 3 == 0:
        s = s + "Pling"
        # is_divisible = True
        
    if number % 5 == 0:
        s = s + "Plang"
        # is_divisible = True

    if number % 7 == 0:
        s = s + "Plong"
        # is_divisible = True

    # if is_divisible:
    if s == "":
        s = str(number)

    return s