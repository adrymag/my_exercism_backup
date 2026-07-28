# brackets [], braces {}, parentheses ()
delimiters = "[]{}()"

def is_paired(input_string):
    """
    Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, 
    verify that any and all pairs are matched and nested correctly. Any other characters should be ignored. 
    For example, "{what is (42)}?" is balanced and "[text}" is not.
    """
    s = "".join([c for c in input_string if c in delimiters])

    if not(s.count("(") == s.count(")")) or not(s.count("[") == s.count("]"))  or not(s.count("{") == s.count("}")):
         return False

    while (s.count("()") + s.count("[]") + s.count("{}") > 0):
        s = s.replace("()","").replace("[]","").replace("{}", "")

    if s == "": # len(s) == 0: # s.replace("()","").replace("[]","").replace("{}", "")
        return True
    
    return False