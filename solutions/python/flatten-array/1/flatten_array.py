# from collection.abc import Iterable

not_atomic_yet = True

def get_next_level(iterable):
    list = []
    not_atomic_yet = False

    for elem in iterable:
        if elem is not None:
            if hasattr(elem, '__iter__'):
                not_atomic_yet = True
                if len(elem) > 0:
                    list.extend(elem)
            else:
                list.append(elem)
    return list

def flatten(iterable):
    """Takes a nested array of any depth and return a fully flattened array.

    Note that some language tracks may include null-like values in the input array, and the way these values are represented varies by track. Such values should be excluded from the flattened array.
    
    Additionally, the input may be of a different data type and contain different types, depending on the track.
    
    Check the test suite for details.
    
    Example
    input: [1, [2, 6, null], [[null, [4]], 5]]
    
    output: [1, 2, 6, 4, 5]

    Parameters:
        iterable (iterable/list): The nested iterable/array.

    Returns:
        list: The fully flattened array/list.
    """
    # flat = []
    previous_level = []
    current_level = iterable
    not_atomic_yet = True
    level_no = 0

    while not_atomic_yet and previous_level != current_level:
        level_no = level_no + 1
        previous_level = current_level
        current_level = get_next_level(current_level)
        print("level no. ")
        print(level_no)
        print(current_level)     
           
    return current_level