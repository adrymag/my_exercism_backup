allergens = {
    'eggs' : 1,
    'peanuts' : 2,
    'shellfish' : 4,
    'strawberries' : 8,
    'tomatoes' : 16,
    'chocolate' : 32,
    'pollen' : 64,
    'cats' : 128
}

allergens2 = {
    'eggs' : 0,
    'peanuts' : 1,
    'shellfish' : 2,
    'strawberries' : 3,
    'tomatoes' : 4,
    'chocolate' : 5,
    'pollen' : 6,
    'cats' : 7
}

allergens4 = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

def base2representation(n): # is_allergy_present # is_alergic_to
    digit_pos = 0
    is_present = [0 for x in range(8)]
    
    while n > 0 and digit_pos <= 7:
        if n%2 == 1:
            is_present[digit_pos] = 1
        else:
            is_present[digit_pos] = 0
        n = int(n/2)
        digit_pos += 1
    return is_present    

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if self.score == 0:
            return False
        
        # is_alergic_to = base2representation(self.score)[allergens2[item]]        
        if base2representation(self.score)[allergens2[item]] == 1:
            return True
        
        return False

    @property
    def lst(self):
        if self.score == 0:
            return []
        
        allergens_list = []
        
        is_alergic_to = base2representation(self.score)

        for alergen_index, is_present in enumerate(is_alergic_to):
            if is_present == 1:
                allergens_list.append(allergens4[alergen_index])
        
        return allergens_list