"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.

    Returns:
        str: The title string in title case (first letters capitalized).
    """
    # The str.title() method parses the string and capitalizes the first
    # character of each word, according to the language/locale rules.
    # It returns a new string because strings are immutable in Python.
    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.

    Returns:
        bool: Is the sentence punctuated correctly?
    """
    # The str.endswith() method returns True if the string ends with the
    # specified suffix (in this case, a period '.'), and False otherwise.
    # This verifies the sentence has proper closing punctuation.
    return sentence.endswith('.')


def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.

    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """
    # The str.strip() method with no arguments removes all combinations of
    # whitespace code points (spaces, tabs, newlines, etc.) from both the
    # beginning and the end of the string. It returns a new string.
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: Input sentence with new words in place of old words.
    """
    # The str.replace() method returns a copy of the string where all
    # occurrences of <old_word> are replaced with <new_word>.
    # This is useful for swapping out adjectives with better synonyms.
    return sentence.replace(old_word, new_word)