def square_root(number):
    decimal_representation = str(number)
    decimal_representation_length = len(decimal_representation)
    # first_digit = int( number / 10 ** ( decimal_representation_length - 1 ) )
    first_digit = int(decimal_representation[0])
    print(first_digit)
    s = 0
    s2 = 0

    if decimal_representation_length % 2 == 1:
        sqrt_decimal_representation_length = (decimal_representation_length + 1) / 2
        if first_digit <= 3:
            s = 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1
        elif first_digit <= 9:
            s = 2 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 2 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1
        else:
            s = 3 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 3 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1


    if decimal_representation_length % 2 == 0:
        sqrt_decimal_representation_length = decimal_representation_length / 2
        if first_digit == 1: # first sqrt digit in [3, 4]
            s = 3 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 4 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1
        if first_digit == 2: # first sqrt digit in [4, 5]
            s = 4 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 5 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1
        if first_digit == 3: # first sqrt digit in [5, 6]
            s = 5 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 6 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1
        if first_digit in {4, 5}: # first sqrt digit in [6, 7]
            s = 6 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 7 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1
        if first_digit in {6, 7}: # first sqrt digit in [6, 7, 8]
            s = 6 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 8 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1
        if first_digit in {8, 9}: # first sqrt digit in [7, 8, 9]
            s = 7 * 10 ** ( sqrt_decimal_representation_length - 1 )
            s2 = 9 * 10 ** ( sqrt_decimal_representation_length - 1 ) + 10 ** ( sqrt_decimal_representation_length - 1 ) - 1

    if s ** 2 == number:
        return s

    if s2 ** 2 == number:
        return s2
    
    while s ** 2 != number and s2 ** 2 != number:
        print([s, s2])

        s1 = int((s + s2) / 2)
        cs = s1 ** 2
        if cs < number:
            s = s1
        elif cs > number:
            s2 = s1
        else:
            return s1

    return -1