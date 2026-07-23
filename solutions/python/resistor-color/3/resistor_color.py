colors_dict = {"black" : 0,
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

def color_code(color):
    """Look up the numerical value associated with a particular color band
    
    Parameters:
        color (str): The color (name) (string).

    Returns:
        int: The value of the associated color code.

    These colors are encoded as follows:

   If you want to build something using a Raspberry Pi, you'll probably use resistors. For this exercise, you need to know two things about them:

    Each resistor has a resistance value.
    Resistors are small - so small in fact that if you printed the resistance value on them, it would be hard to read.
    To get around this problem, manufacturers print color-coded bands onto the resistors to denote their resistance values. Each band has a position and a numeric value.
    black: 0
    brown: 1
    red: 2
    orange: 3
    yellow: 4
    green: 5
    blue: 6
    violet: 7
    grey: 8
    white: 9
    """

    # code = colors_dict[color]    
    return colors_dict[color] # code

def colors():
    """list the different band colors
    
    Returns:
            list: The list of color names.
    """
    return list(colors_dict.keys())