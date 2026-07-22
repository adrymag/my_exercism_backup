def line_up(name, number):
    """
    Given a name and a number, your task is to produce a sentence using that name and that number as an ordinal numeral. Yaʻqūb expects to use numbers from 1 up to 999.
    
    Rules:
    
    Numbers ending in 1 (unless ending in 11) → "st"
    Numbers ending in 2 (unless ending in 12) → "nd"
    Numbers ending in 3 (unless ending in 13) → "rd"
    All other numbers → "th"
    Examples:
    
    "Mary", 1 → "Mary, you are the 1st customer we serve today. Thank you!"
    "John", 12 → "John, you are the 12th customer we serve today. Thank you!"
    "Dahir", 162 → "Dahir, you are the 162nd customer we serve today. Thank you!"
    """

    last_digit = number % 10
    last_2_digits = number % 100
    
    if last_digit == 1 and last_2_digits != 11:
        termination = "st"
    elif last_digit == 2 and last_2_digits != 12:
        termination = "nd"
    elif last_digit == 3 and last_2_digits != 13:
        termination = "rd"
    else:
        termination = "th"

    return name + ", you are the " + str(number) + termination + " customer we serve today. Thank you!"