def strip_punctuation(s):
    for c in ["'", '-', '!', '.', ';', ',', ':', '?', ' ']:
        s = s.replace(c, '')    
    return s

def strip_letters(s):
    s = s.lower()
    is_iso = True
    
    for c in s:
        l = len(s)
        if 97 <= ord(c) and ord(c) <= 122:
            s = s.replace(c, '')
            if len(s) < l - 1 and is_iso:
                is_iso = False

    return [s, is_iso]

def is_isogram(phrase):
    """Determine if a word or phrase is an isogram.

    An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
    
    Examples of isograms:
    
    lumberjacks
    background
    downstream
    six-year-old
    The word isograms, however, is not an isogram, because the s repeats.
    """
    phrase = strip_punctuation(phrase)
    [letters_stripped_phrase, is_iso] = strip_letters(phrase)
    
    if is_iso and letters_stripped_phrase.strip() == "":
        return True
    # if phrase.isalpha()
    return False