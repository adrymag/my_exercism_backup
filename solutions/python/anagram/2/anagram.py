def find_anagrams(word, candidates):
    """Finds all anagrams of word in given candidates

    Parameters:
        word (str): The word.
        candidates (list): The list of items to search.

    Returns:
        list: The list of found anagrams.    
    """
    if candidates == []:
        return []
    
    word = word.lower()
    # bad_candidates = [candidate for candidate in candidates if candidate.lower() == word]
    # candidates.remove(bad_candidates)
    candidates = [candidate for candidate in candidates if not candidate.lower() == word]

    if candidates == []:
        return []

    anagrams = []
    word_letters = set(word)
    letters_occurrences_in_word = {}
    
    for letter in word:
        letters_occurrences_in_word[letter] = word.count(letter)
    
    for current_candidate in candidates:
        is_anagram = True
        current_candidate_lower = current_candidate.lower()
        current_candidate_letters = set(current_candidate_lower)
        if current_candidate_letters == word_letters:
            for letter in current_candidate_letters:
                if current_candidate_lower.count(letter) != letters_occurrences_in_word[letter]:
                    is_anagram = False
                    break
            if is_anagram: 
                anagrams.append(current_candidate)
            
    return anagrams