def rebase(input_base, digits, output_base):
    """
    Converts a number from one base to another

    Parameters:
        input_base (int): The base in which the (initial) number representation is given
        digits (list): The representation of the number in the base input_base
        output_base: The base output_base ( in which the output representation of number is requested / should be provided )

    Returns:
        list: The representation of the number in the base output_base.
    """
    if input_base < 2 :
        raise ValueError("input base must be >= 2")
    
    if output_base < 2 :
        raise ValueError("output base must be >= 2")

    representation_length = len(digits)
    
    # if representation_length <= 0:
        # raise ValueError("input representation ( in input_base ) must be non-empty")
        # return [0]

    if digits == [0] or digits == []:
        return [0]

    input_value = 0
    # output_base_representation = ""
    output_base_representation = []

    if input_base == 10:
        # input_value = int(str(digits).replace(", ", "")[1:-1])
        input_value = int("".join([str(digit) for digit in digits]))
    else:
        for index, digit in enumerate(digits): # index = 0-based position in base input_base representation
            if digit >= input_base or digit < 0:
                raise ValueError("all digits must satisfy 0 <= d < input base")
            if digit > 0:
                input_value = input_value + digit * input_base ** ( representation_length - 1 - index )

    if input_value == 0:
        return [0]
        
    while input_value > 0:
        current_digit = input_value % output_base
        input_value = int(( input_value - input_value % output_base ) / output_base)
        output_base_representation = [current_digit] + output_base_representation
    return output_base_representation