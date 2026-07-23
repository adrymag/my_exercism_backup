"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 4
EQUAL = 0
UNEQUAL = 1

def is_sublist(list_one, list_two):
    if list_one == []:
        return True
        
    l1 = len(list_one)
    l2 = len(list_two)

    # if len(list_two) <= len(list_one):
    if l2 <= l1:
        return False

    # elem_count_diff = l2 - l1

    for start_pos in range(l2 - l1 + 1):
        if list_one == list_two[start_pos : start_pos + l1]:
            return True

    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    if is_sublist(list_one, list_two): # list_two.includes(list_one): # here length_1 < length_2
            return SUBLIST
        
    if is_sublist(list_two, list_one): # list_one.includes(list_two): # is_sublist_of_first_list
        return SUPERLIST
   
    return UNEQUAL