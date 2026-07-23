# import re

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou" # consonants: the other 21 letters of the English alphabet
alphabet_set = set(alphabet)
vowels_set = set(vowels)
semi_vowels = "yw"
# semi_vowels_set = set(semi_vowels)
consonants_set = set(alphabet) - set(vowels) - set(semi_vowels)
consonants = "".join(consonants_set)
consonants2 = consonants + "y"

# print(consonants)

# def remove_consonants(word):
#     # w = list(word).remove(consonants)
#     return "".join([x for x in word if x not in consonants])

# word = "testul acesta"
# print(remove_consonants(word))

s = "Acesta este un test. Testul acesta ma ajuta sa verific functionarea anumitor functii Python pentru lucrul cu strings."
# p = s.find("a")
# print(p)

# for cp in range(len(s)):
#     p = s.find("a", cp)
#     if p > 0:
#         print(p)

# for i, c in enumerate(s):
#     if c == 'a':
#         print(i)

# positions = [match.start() for match in re.finditer("a", s)]
# positions = list([i for i, c in enumerate(s) if c == 'a'])
# print(positions)

def remove_consonants(word):
    # if word[0] == 'y':
    #     word1 = word[1:]
    # else:
    #     word1 = word

    if word[0] == 'y':
        return "".join([x for x in word if x not in consonants2])
    else:
        return "".join([x for x in word if x not in consonants])

    # return "".join([x for x in word1 if x not in consonants]) # [x for x in word if x not in consonants]
    # return "".join([x for x in word if x not in consonants])


def generate_text_words_mask(text):
    text_mask = ""
    l = len(text)
    in_word = False
    current_word = ""
    words = []

    for current_char_pos, character in enumerate(text):
        if character in alphabet + alphabet.upper() + '-': # word letter
            if not in_word:
                in_word = True
                text_mask += "w"
                current_word = character
            else:
                # 
                current_word += character
        else:
            if in_word:
                words.append(current_word)
            text_mask += character
            in_word = False

    if character in alphabet + alphabet.upper() + '-':
        words.append(current_word)
            
    return [text_mask, words]             

def split_text_in_words(text):
    return text.split(" ")

def appy_rule_1(word):
    if not(word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt"):
        return word
    return word + "ay"

def appy_rule_3(word):
    qu_position = word.find("qu") # has "qu" inside
    if qu_position >= 0:
        qu_prefix = word[0:qu_position]
        if qu_prefix == "" or len(remove_consonants(qu_prefix)) == 0: # has only consonants or nothing (~ 0 or more consonants) in front of "qu"
            return word[qu_position+2:] + word[0:qu_position] + "quay"
    return word    

def appy_rule_4(word):
    if not(word[0] in consonants and remove_consonants(word)[0] == "y"):
        return word
    y_position = word.find("y")
    return word[y_position:] + word[0:y_position] + "ay"

def appy_rule_2(word):
    if not(word[0] in consonants2):
        return word
    first_vowel_position = word.find(remove_consonants(word)[0]) # word[0:first_vowel_position]
    
    return word[first_vowel_position:] + word[0:first_vowel_position] + "ay"

def translateWord(word):
    word1 = appy_rule_1(word)
    if word1 != word:
        return [word1, 1] # translated_words[index] = word1
    word3 = appy_rule_3(word)
    if word3 != word:
        return [word3, 3] # translated_words[index] = word3
    word4 = appy_rule_4(word)
    if word4 != word:
        return [word4, 4] # translated_words[index] = word4
    word2 = appy_rule_2(word)    
    if word2 != word:
        return [word2, 2] # translated_words[index] = word2
    
    return [word, 0] # translated_words[index] = word

def translate(text):
    """Translates text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants:

    vowels: the letters a, e, i, o, and u
    consonants: the other 21 letters of the English alphabet
    
    Rule 1
    If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
    
    For example:
    
    "apple" -> "appleay" (starts with vowel)
    "xray" -> "xrayay" (starts with "xr")
    "yttria" -> "yttriaay" (starts with "yt")
    
    Rule 2
    If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
    
    For example:
    
    "pig" -> "igp" -> "igpay" (starts with single consonant)
    "chair" -> "airch" -> "airchay" (starts with multiple consonants)
    "thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
    
    Rule 3
    If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
    
    For example:
    
    "quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
    "square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")
    
    Rule 4
    If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.
    
    Some examples:
    
    "my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
    "rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")

    Parameters:
        text (str): The source/input English language text (to be translated).

    Returns:
        str: The Pig Latin translation of the source/input English text.

    """
    text_mask1 = generate_text_words_mask(text) # "quick fast run"
    # print(text_mask1[0]) # "w w w"
    # print(text_mask1[1]) # ['quick', 'fast', 'run']
    text_mask = text_mask1[0]
    words_list = text_mask1[1]
    text_mask_separators_list = text_mask.split('w')
    # print(text_mask_separators_list)
    translated_words = [i for i in range(len(words_list))]
    # translated_word_methods = [i for i in range(len(words_list))]

    for index, word in enumerate(words_list):
        translated_word_results = translateWord(word)
        translated_word = translated_word_results[0]
        translated_word_method = translated_word_results[1]
        translated_words[index] = translated_word 
        # translated_word_methods[index] = translated_word_method

    translated_text = ""

    # for i, sep in enumerate(text_mask_separators_list):
    for i, translated_word in enumerate(translated_words):
        translated_text = translated_text + text_mask_separators_list[i]
        translated_text = translated_text + translated_words[i]
        # translated_word_methods_str = translated_word_methods_str.append(translated_word_methods[i])

    translated_text = translated_text + text_mask_separators_list[i+1]     

    print(translated_text) # "ickquay astfay unray"    
    # print(translated_word_methods) # [3, 2, 2]

    return translated_text