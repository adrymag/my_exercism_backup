def is_pangram(sentence):
    """Figure out if a sentence is a pangram.

    A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
    
    For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.

    Parameters:
        sentence (str): The sentence being checked (for pangrammacy).

    Returns:
        bool: True if it's a pangram, False otherwise.
    """
    
    s = {' '}

    for c in sentence.lower():
        if 97 <= ord(c) <= 122:
            s.add(c)

    if len(s) == 27:
        return True
        
    return False