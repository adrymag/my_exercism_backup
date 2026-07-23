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