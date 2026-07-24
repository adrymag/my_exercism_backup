def slices(series, length):
    """Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.
    """
    # if the slice length is zero.
    if length == 0:
        raise ValueError("slice length cannot be zero")
    # if the slice length is negative.
    if length < 0:
        raise ValueError("slice length cannot be negative")
    # if the series provided is empty.
    if series == [] or series is None or series == "":
        raise ValueError("series cannot be empty")
    l = len(series)
    
    # if the slice length is longer than the series.
    if l < length:
        raise ValueError("slice length cannot be greater than series length")
    if l == length:
        return[series]
        
    if length == 1:
        return list(series)
    return [series[start_pos : start_pos + length] for start_pos in range(len(series) - length + 1)]


def product_of_2_numbers(a, b):
    return int(a) * int(b)
    

def foldl(function, list, initial):
    r = initial
    # [r := function(r, e) for e in list]
    for e in list:
        r = function(r, e)
    # r = function(r, initial)
    return r
    
    
def foldr(function, list, initial):
    r = initial
    # [r := function(e, r) for e in reversed(list)]
    for e in reversed(list):
        r = function(r, e)
    # r = function(initial, r)
    return r
    

def largest_product(series, size):
    # span of numbers is longer than number series
    if len(series) < size:
        raise ValueError("span must not exceed string length")
    
    # span of number is negative
    if size < 0:
        raise ValueError("span must not be negative")
    
    # series includes non-number input
    if len([x for x in series if not x.isnumeric()]) > 0:
        raise ValueError("digits input must only contain digits")

    sequences = slices(series, size)

    max_prod = 0

    for s in sequences:
        p = foldl(product_of_2_numbers, s, 1)
        if p > max_prod:
            max_prod = p

    return max_prod