# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

ANY_COMBINATION = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]
EMPTY_LIST = []

def score(dice, category):
    if category in ANY_COMBINATION:
        score_factor = [x + 1 for x in range(len(ANY_COMBINATION)) if ANY_COMBINATION[x] == category][0] # multiplier
        return score_factor * len([x for x in dice if x == score_factor])
    if category == FULL_HOUSE:
        triple_factor = [x for x in set(range(1, 7)) if dice.count(x) == 3]
        double_factor = [x for x in set(range(1, 7)) if dice.count(x) == 2]
        if not(triple_factor == []) and not(double_factor == []):
            # len(triple_factor) > 0 and len(double_factor) > 0:
            # EMPTY_LIST not in {double_factor, triple_factor}: # cannot use 'list' as a set element (Unhashable type: 'list')
            return 3 * triple_factor[0] + 2 * double_factor[0] # sum(dice)
        else:
            return 0
    if category == FOUR_OF_A_KIND:
        quad_factor = [x for x in set(range(1, 7)) if dice.count(x) in {4, 5}] # quadruple_factor
        if quad_factor == EMPTY_LIST:
            return 0
        else:  # len(quad_factor) > 0:
            return 4 * quad_factor[0]
    if category == LITTLE_STRAIGHT:
        if set(dice) == set(list(range(1, 6))):
            return 30
        else:
            return 0
    if category == BIG_STRAIGHT:
        if set(dice) == set(list(range(2, 7))):
            return 30
        else:
            return 0
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    if category == CHOICE:
        return sum(dice) # dice.sum()