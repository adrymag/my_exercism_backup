def equilateral(sides):
    """Checks whether the given numbers can be the lenghts of the sides of an equilateral triangle.
    Parameters:
        sides (list[float]): The list of 3 numbers representing the lengths of the sides.

    Returns:
        bool: True if the given numbers can be the lenghts of the sides of an equilateral triangle, False otherwise.
    """
    [side_1, side_2, side_3] = sides
    
    return is_triangle(sides) and ( side_1== side_2 and side_2 == side_3 )


def isosceles(sides):
    """Checks whether the given numbers can be the lenghts of the sides of an isosceles triangle.
    Parameters:
        sides (list[float]): The list of 3 numbers representing the lengths of the sides.

    Returns:
        bool: True if the given numbers can be the lenghts of the sides of an isosceles triangle, False otherwise.
    """
    [side_1, side_2, side_3] = sides
    
    return is_triangle(sides) and ( side_1 == side_2 or side_2 == side_3 or side_3 == side_1 )


def scalene(sides):   
    """Checks whether the given numbers can be the lenghts of the sides of a scalene (non-isosceles) triangle.
    Parameters:
        sides (list[float]): The list of 3 numbers representing the lengths of the sides.

    Returns:
        bool: True if the given numbers can be the lenghts of the sides of a scalene (non-isosceles) triangle, False otherwise.
    """
    return is_triangle(sides) and not isosceles(sides) # not( side_1 == side_2 or side_2 == side_3 or side_3 == side_1 )


def is_triangle(sides):
    """Checks whether the given numbers can be the lenghts of the sides of a (non-degenerate) triangle.
    Parameters:
        sides (list[float]): The list of 3 numbers representing the lengths of the sides.

    Returns:
        bool: True if the given numbers can be the lenghts of the sides of a (non-degenerate) triangle, False otherwise.
    """
    [side_1, side_2, side_3] = sides

    return ( side_1 + side_2 > side_3 ) and ( side_2 + side_3 > side_1 ) and ( side_3 + side_1 > side_2 )