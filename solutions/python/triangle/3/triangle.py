def equilateral(sides):
    [side_1, side_2, side_3] = sides
    
    return is_triangle(sides) and ( side_1== side_2 and side_2 == side_3 )


def isosceles(sides):
    [side_1, side_2, side_3] = sides
    
    return is_triangle(sides) and ( side_1 == side_2 or side_2 == side_3 or side_3 == side_1 )


def scalene(sides):   
    return is_triangle(sides) and not isosceles(sides) # not( side_1 == side_2 or side_2 == side_3 or side_3 == side_1 )


def is_triangle(sides):
    [side_1, side_2, side_3] = sides

    return ( side_1 + side_2 > side_3 ) and ( side_2 + side_3 > side_1 ) and ( side_3 + side_1 > side_2 )