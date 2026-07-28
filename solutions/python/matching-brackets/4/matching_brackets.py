# brackets [], braces {}, parentheses ()
delimiters = "[]{}()"

def is_paired(input_string):
    """
    Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, 
    verify that any and all pairs are matched and nested correctly. Any other characters should be ignored. 
    For example, "{what is (42)}?" is balanced and "[text}" is not.
    """
    s = "".join([c for c in input_string if c in delimiters])

    # if not(s.count("(") == s.count(")")) or not(s.count("[") == s.count("]"))  or not(s.count("{") == s.count("}")):
         # return False

    stop = False
    prev_length = len(s)
    
    while not(stop):
        s = s.replace("()","").replace("[]","").replace("{}", "")
        new_length = len(s)
        if new_length < prev_length:
            prev_length = new_length
        else:
            stop = True

    if s == "": # len(s) == 0: # s.replace("()","").replace("[]","").replace("{}", "")
        return True
    
    return False