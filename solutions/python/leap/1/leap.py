def leap_year(year):
    """Determines whether the given number represents a leap year or not.
    A leap year (in the Gregorian calendar) occurs:

    In every year that is evenly divisible by 4, unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.

    Parameters:
        year (int): The year (number).

    Returns:
        bool: True if it's a leap year, False otherwise.
    """
    return ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0