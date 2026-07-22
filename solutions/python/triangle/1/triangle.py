def equilateral(sides):
    [a,b,c] = sides
    
    return is_triangle(sides) and ( a == b and b == c )


def isosceles(sides):
    [a,b,c] = sides
    
    return is_triangle(sides) and ( a == b or b == c or c == a )


def scalene(sides):
    [a,b,c] = sides
    
    return is_triangle(sides) and not isosceles(sides) # not( a == b or b == c or c == a )


def is_triangle(sides):
    [a,b,c] = sides

    return ( a + b > c ) and ( b + c > a ) and ( c + a > b )