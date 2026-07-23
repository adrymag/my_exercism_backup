def append(list1, list2):
    # [list1.insert(e) for e in list2]
    list1.extend(list2)
    return list1


def concat(lists):
    if lists == []:
        return []

    if len([l for l in lists if l != []]) == 0:
        return []
       
    list = []
    # [list.append(e) for e in l for l in lists]
    [list.extend(l) in l for l in lists]
    return list


def filter(function, list):    
    return [e for e in list if function(e)]


def length(list):
    # l = 0
    return sum([1 for e in list]) # max( [i for i, e in enumerate(list)] ) + 1


def map(function, list):
    return [function(e) for e in list]


def foldl(function, list, initial):
    r = initial
    # [r := function(r, e) for e in list]
    for e in list:
        r = function(r, e)
    # r = function(r, initial)
    return r


def foldr(function, list, initial):
    r = initial
    # [r := function(e, r) for e in reversed(list)]
    for e in reversed(list):
        r = function(r, e)
    # r = function(initial, r)
    return r

def reverse(list):
    return list[::-1] # [list[-i - 1] for i in range(len(list))]