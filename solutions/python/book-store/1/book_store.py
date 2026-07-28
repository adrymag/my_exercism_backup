"""
Book Store — Exercism Python Track

A bookshop offers discounts on bulk purchases of different titles from a
5-book series.  One copy of any book costs $8.  The discounts are:

    2 different books  →  5%  discount
    3 different books  →  10% discount
    4 different books  →  20% discount
    5 different books  →  25% discount

The twist: the discount applies only to sets of *different* titles.  If you
buy 4 books but only 3 are unique, the 3 unique ones get the 10% discount
and the duplicate costs full price.

The challenge is to group the books into sets so that the total price is
minimised.  A naïve greedy strategy ("always make the biggest set possible")
is not optimal.  For example:

    Basket: 2×book-1, 2×book-2, 2×book-3, 1×book-4, 1×book-5

    Greedy:  one 5-set + one 3-set  →  $30.00 + $21.60 = $51.60
    Optimal: two 4-sets              →  $25.60 + $25.60 = $51.20

We solve this with dynamic programming (DP) over the multiset of remaining
book counts.  Because there are only 5 titles, the state space is tiny and
memoised recursion is both simple and guaranteed optimal.
"""

from functools import lru_cache


def total(basket):
    """Return the minimum possible price (in cents) for the given basket.

    Args:
        basket (list[int]): A list of book numbers (1–5) representing the
            shopping basket.

    Returns:
        int: Total price in cents.  (We work in cents to avoid floating-point
            rounding issues; $8.00 becomes 800 cents.)

    Approach — Dynamic Programming with Memoisation
    -----------------------------------------------
    1. Count how many copies of each title (1–5) are in the basket.
    2. Sort the counts descending.  This gives a *canonical state*:
       e.g. (2, 2, 2, 1, 1) means two titles appear twice and three titles
       appear once (the zeros are implicit).  Sorting makes the state
       hashable and eliminates redundant permutations — the order of titles
       does not matter, only the multiset of counts.
    3. Define dp(state) = minimum cost to buy all remaining books.
       Base case: all counts are zero → cost 0.
       Recurrence: try every possible group size k (1 to number of
       remaining titles).  Form a group of k different books by taking
       one copy from each of the k most abundant titles, then recurse.
       dp(state) = min over k of (cost_of_k_group + dp(state_after_k))
    4. Pre-compute the cost of each group size to avoid repeating the
       arithmetic.
    """

    # -----------------------------------------------------------------------
    # Edge case: empty basket costs nothing.
    # -----------------------------------------------------------------------
    if not basket:
        return 0

    # -----------------------------------------------------------------------
    # Step 1 — Count frequencies of each title (1 through 5).
    # -----------------------------------------------------------------------
    counts = [0] * 5
    for book in basket:
        counts[book - 1] += 1

    # -----------------------------------------------------------------------
    # Step 2 — Normalise the state by sorting counts descending.
    #
    # All books are interchangeable from a pricing perspective; only the
    # multiset of counts matters.  Sorting gives us a canonical tuple that
    # can be hashed and used as a memoisation key.
    # -----------------------------------------------------------------------
    initial_state = tuple(sorted(counts, reverse=True))

    # -----------------------------------------------------------------------
    # Pre-compute group costs in cents.
    #
    # Base price = 800 cents ($8.00).
    # Discounts are applied to the whole group.
    # We use integer arithmetic throughout to stay exact.
    # -----------------------------------------------------------------------
    BASE_PRICE = 800
    DISCOUNTS = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}
    group_cost = {
        k: k * BASE_PRICE * (100 - DISCOUNTS[k]) // 100
        for k in DISCOUNTS
    }

    # -----------------------------------------------------------------------
    # Step 3 — Memoised recursive DP.
    # -----------------------------------------------------------------------
    @lru_cache(maxsize=None)
    def dp(state):
        """Return the minimum cost to clear all books described by `state`.

        Args:
            state (tuple[int]): Sorted counts of each title, descending.

        Returns:
            int: Minimum cost in cents.
        """
        # Base case: nothing left to buy.
        if all(c == 0 for c in state):
            return 0

        best = float('inf')

        # How many distinct titles still have at least one copy?
        num_types = sum(1 for c in state if c > 0)

        # Try forming a group of every possible size from 1 up to the number
        # of remaining distinct titles.
        for k in range(1, num_types + 1):
            # Create the next state by removing one copy from each of the
            # k most abundant titles (the first k entries in the sorted
            # tuple).  Because the tuple is sorted, these are guaranteed to
            # be positive.  After decrementing we re-sort to maintain the
            # canonical representation.
            new_state = list(state)
            for i in range(k):
                new_state[i] -= 1
            new_state = tuple(sorted(new_state, reverse=True))

            # Total cost = cost of this group + optimal cost of remainder.
            candidate = group_cost[k] + dp(new_state)
            if candidate < best:
                best = candidate

        return best

    # -----------------------------------------------------------------------
    # Step 4 — Kick off the recursion from the initial basket state.
    # -----------------------------------------------------------------------
    return dp(initial_state)