def is_armstrong_number(number):
    """Determine if the input number is an Armstrong number 
    (also called narcissistic number or known as a pluperfect digital invariant (PPDI),),
    i.e. a number that equals the sum of its digits raised to the total number of its digits.
    
    Examples:

    9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

    https://en.wikipedia.org/wiki/Narcissistic_number

    Parameters:
        number (int): The number being checked.

    Returns:
        bool: True if narcissistic, False if not.    
    """
    n = number
    l = 1 # length of n's decimal representation = no of digits in n = floor(lg(n)) + 1 # log(n) # log10(n)
    while n >= 10:
        n = n/10
        l = l + 1

    n = number
    s = 0   
    ns = ""
    
    while n >= 10:
        d = n % 10 # last digit in n
        ns = ns + str(d)
        s = s + ( d ** l )
        n = (n - d) / 10 # (n - n % 10)/10 
        if s > number:
            return False # str(s) + " > " + str(number) + " ( of " + str(l) + " digits ), checking ns : " + ns + ", checking last digit : " + str(d) # 

    s = s + n ** l
        
    if s == number:
        return True # str(number) + " is A/N." + " ( of " + str(l) + " digits )"

    return False # str(s) + " <> " + str(number) + " ( of " + str(l) + " digits )"