def score(x, y):
    """Calculate the points scored in a single toss of a Darts game.

    If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points.
    
        The outer circle has a radius of 10 units (this is equivalent to the total radius for the entire target), 
        the middle circle a radius of 5 units, 
        and the inner circle a radius of 1. 
    Of course, they are all centered at the same point — that is, the circles are concentric defined by the coordinates (0, 0).

    Given a point in the target (defined by its Cartesian coordinates x and y, where x and y are real), 
    calculate the correct score earned by a dart landing at that point.

    Parameters:
        (x, y) (float, float): The coordinates of the toss(ed) point.

    Returns:
        int: Number of pointa awarded for that toss.
    """
    if x ** 2 + y ** 2 > 10 ** 2 :
        return 0
    if x ** 2 + y ** 2 <= 1 ** 2 :
        return 10
    if x ** 2 + y ** 2 <= 5 ** 2 :
        return 5
    return 1