colors_dict = {
                    "black" : 0,
                    "brown" : 1,
                    "red" : 2,
                    "orange" : 3,
                    "yellow" : 4,
                    "green" : 5,
                    "blue" : 6,
                    "violet" : 7,
                    "grey" : 8,
                    "white" : 9
                  }

measure_units_scale = {
                        0: "",
                        1 : "kilo",
                        2 : "mega",
                        3 : "giga"
                      }

def value(colors):
    """
    The first 2 bands of a resistor have a simple encoding scheme: each color maps to a single number. For example, if they printed a brown band (value 1) followed by a green band (value 5), it would translate to the number 15.

    Parameters:
        colors (list): The list of colors associated with the current set of resistors.

    Returns:
        int: The code associated with the first 2 colors from the input list.
    """

    return colors_dict[colors[0]] * 10 + colors_dict[colors[1]]

def label(colors):
    """
    The first 3 bands of a resistor have a simple encoding scheme: each color maps to a single number, the encoding of the duo formed by the first 2 colors is determined first, and then a number of zeros (0 digits) equal to the code of the third color is appended to it.

    Parameters:
        colors (list): The list of colors associated with the current set of resistors.

    Returns:
        str: The code associated with the first 3 colors from the input list (terminated with the suffix "ohms" ( with "kilo" or "mega" or "giga" in front of it, in case thousands or millions or billions of ohms are encountered/...
    """
    if colors_dict[colors[0]] + colors_dict[colors[1]] + colors_dict[colors[2]] == 0:
        return "0 ohms"

    if colors_dict[colors[1]] == 0: # secoind color = black
        return str(colors_dict[colors[0]]) + "0" * ( ( colors_dict[colors[2]] + 1 ) % 3 ) + " " + measure_units_scale[ int( ( ( colors_dict[colors[2]] + 1 ) - ( colors_dict[colors[2]] + 1 ) % 3 ) / 3 ) ] + "ohms"
    else:
        return str(value(colors)) + "0" * ( colors_dict[colors[2]] % 3 ) + " " + measure_units_scale[ int(( colors_dict[colors[2]] - colors_dict[colors[2]] % 3 ) / 3) ] + "ohms"