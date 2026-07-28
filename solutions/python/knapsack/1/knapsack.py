"""
Knapsack — Exercism Python Track (0/1 Knapsack)

Lhakpa the Sherpa guide must choose which items to carry in her knapsack.
Each item has a weight and a strictly positive value. She can take each item
at most once, and the total weight must not exceed the knapsack's capacity.

The goal is to maximise the total value of the selected items.

This is the classic *0/1 Knapsack* problem, solved here with dynamic
programming (DP) in O(n × W) time and O(W) space, where n is the number
of items and W is the maximum weight capacity.
"""


def maximum_value(maximum_weight, items):
    """Return the maximum total value achievable without exceeding the weight limit.

    Args:
        maximum_weight (int): The knapsack's weight capacity.
        items (list[dict]): A list of items, each a dict with keys:
            - "weight" (int): How much the item weighs.
            - "value"  (int): How much the item is worth.

    Returns:
        int: The maximum possible total value.

    Approach — Dynamic Programming (1-D array)
    ------------------------------------------
    We maintain a 1-D array `dp` where:

        dp[w] = maximum value achievable with weight limit exactly w
                (or less, since we never force the limit to be tight).

    Initially dp is all zeros because with no items selected the value is 0
    for every possible weight limit.

    For each item we consider whether adding it improves any achievable weight.
    The crucial detail is that we iterate weights *backwards* (from
    maximum_weight down to the item's weight).  This guarantees that each
    item is used at most once: when we read dp[w - weight] we are looking at
    the state *before* the current item was considered, not after.

    If we iterated forwards we would be doing the *unbounded* knapsack
    (items can be taken multiple times), which is not what we want.

    The recurrence is:

        dp[w] = max(dp[w], dp[w - item_weight] + item_value)

    After processing all items, dp[maximum_weight] holds the answer.
    """

    # -----------------------------------------------------------------------
    # Edge case: no items or zero capacity.
    # There is nothing to carry, so the best value is 0.
    # -----------------------------------------------------------------------
    if not items or maximum_weight <= 0:
        return 0

    # -----------------------------------------------------------------------
    # dp[w] will hold the best value achievable with weight limit w.
    # We only need a 1-D array of length (maximum_weight + 1).
    # Index 0 represents capacity 0 (value 0), index W represents capacity W.
    # -----------------------------------------------------------------------
    dp = [0] * (maximum_weight + 1)

    # -----------------------------------------------------------------------
    # Process every item one at a time.
    # -----------------------------------------------------------------------
    for item in items:
        weight = item["weight"]
        value = item["value"]

        # If the item itself is heavier than the knapsack can ever hold,
        # skip it immediately — it can never be part of any valid solution.
        if weight > maximum_weight:
            continue

        # -------------------------------------------------------------------
        # Update the DP table for this item.
        #
        # We walk backwards from maximum_weight down to weight.
        # Why backwards? Because dp[w - weight] must refer to the state
        # *before* this item was added.  If we walked forwards, we might
        # read a cell that already includes the current item, leading to
        # using the same item multiple times (unbounded knapsack).
        #
        # For every capacity w that can accommodate this item, we ask:
        #   "Is the current best value for capacity w improved by taking
        #    this item plus the best value for the remaining capacity
        #    (w - weight)?"
        #
        # We take the maximum of "don't take the item" (dp[w]) and
        # "take the item" (dp[w - weight] + value).
        # -------------------------------------------------------------------
        for w in range(maximum_weight, weight - 1, -1):
            candidate = dp[w - weight] + value
            if candidate > dp[w]:
                dp[w] = candidate

    # -----------------------------------------------------------------------
    # After all items have been considered, dp[maximum_weight] contains the
    # maximum value achievable with total weight at most maximum_weight.
    # -----------------------------------------------------------------------
    return dp[maximum_weight]