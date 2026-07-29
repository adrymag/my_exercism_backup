def find_anagrams(word, candidates):
    if candidates == []:
        return []
    
    word = word.lower()
    # bad_candidates = [candidate for candidate in candidates if candidate.lower() == word]
    # candidates.remove(bad_candidates)

    candidates = [candidate for candidate in candidates if not candidate.lower() == word]
    candidates_lower = [candidate.lower() for candidate in candidates]

    # if word in candidates_lower:
    #     candidates_lower.remove(word)

    if candidates == []:
        return []

    anagrams = []
    word_letters = set(word)
    letters_occurrences_in_word = {}
    
    for letter in word:
        letters_occurrences_in_word[letter] = word.count(letter)
    
    for candidate_index, current_candidate in enumerate(candidates):
        is_anagram = True
        current_candidate_lower = candidates_lower[candidate_index] # current_candidate.lower
        current_candidate_letters = set(current_candidate_lower)
        if current_candidate_letters == word_letters:
            for letter in current_candidate_letters:
                if current_candidate_lower.count(letter) != letters_occurrences_in_word[letter]:
                    is_anagram = False
                    break
            if is_anagram: 
                anagrams.append(current_candidate)
            
    return anagrams