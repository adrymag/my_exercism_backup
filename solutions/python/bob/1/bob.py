def strip_punctuation(s):
    for c in ["'", '-', '!', '.', ';', ',', ':', '?', ' ']:
        s = s.replace(c, '')    
    return s

def has_letters(s):
    for c in s:
        if isalpha(c):
            return True
    return False
    
def response(hey_bob):
    """Determines what Bob will reply to someone when they say something to him or ask him a question.

    Bob only ever answers one of five things:
    
    "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    "Whatever." This is what he answers to anything else.

    Parameters:
        hey_bob (str): The message sent to Bob.

    Returns:
        str: Bob's reply.
    """
    # and hey_bob.strip().isalnum() and not(hey_bob.strip().isnumeric())

    hey_bob = hey_bob.strip()
    is_question = hey_bob.endswith('?')
    hey_bob = strip_punctuation(hey_bob)

    if is_question and hey_bob.upper() == hey_bob and hey_bob.isalnum() and not(hey_bob.isnumeric()): # a question, but not with no letters, so an all capitals one..
        return "Calm down, I know what I'm doing!"
    if is_question: # other types of questions, not all capitals (ones..)
        return "Sure."
    if hey_bob == "": # length(hey_bob.trim()) == 0:
        return "Fine. Be that way!"
    if hey_bob.upper() == hey_bob and not(hey_bob.isnumeric()): # all capitals, with letters, not a question
        return "Whoa, chill out!"       
    return "Whatever."