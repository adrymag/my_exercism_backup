"""
Proverb — Exercism Python Track

Generate the traditional "For Want of a Nail" proverb from a list of items.

Given a sequence of inputs, each line links consecutive items:

    For want of a {current} the {next} was lost.

The final line names the very first item as the root cause:

    And all for the want of a {first}.

If a `qualifier` is provided, it is inserted before the first item in the
final line:

    And all for the want of a {qualifier} {first}.

An empty input produces an empty list.
"""


def proverb(*items, qualifier=None):
    """Generate the proverb lines from the given items.

    Args:
        *items: A variable-length sequence of strings, each naming a thing
            that was lost because the previous thing was missing.
        qualifier (str | None): An optional modifier for the first item in
            the final verse.  If given, the final line reads
            "And all for the want of a {qualifier} {first}."

    Returns:
        list[str]: The proverb as a list of sentences, one per line.
    """
    # -----------------------------------------------------------------------
    # Edge case: no items means there is nothing to say.
    # -----------------------------------------------------------------------
    if not items:
        return []

    # -----------------------------------------------------------------------
    # Build the body of the proverb.
    #
    # We pair each item with its successor using zip(items, items[1:]).
    # For ["nail", "shoe", "horse"] this yields:
    #   ("nail", "shoe")  →  "For want of a nail the shoe was lost."
    #   ("shoe", "horse") →  "For want of a shoe the horse was lost."
    #
    # The zip naturally stops at the shorter sequence, so we get exactly
    # len(items) - 1 lines.
    # -----------------------------------------------------------------------
    lines = [
        f"For want of a {current} the {next_item} was lost."
        for current, next_item in zip(items, items[1:])
    ]

    # -----------------------------------------------------------------------
    # Append the concluding line.
    #
    # If a qualifier was supplied, it prefixes the first item:
    #   qualifier="horseshoe", first="nail"
    #   → "And all for the want of a horseshoe nail."
    #
    # Otherwise the first item stands alone:
    #   → "And all for the want of a nail."
    #
    # We use `qualifier is not None` so that an empty string qualifier
    # still produces a space-separated prefix (rather than being ignored).
    # -----------------------------------------------------------------------
    first = items[0]
    if qualifier is not None:
        lines.append(f"And all for the want of a {qualifier} {first}.")
    else:
        lines.append(f"And all for the want of a {first}.")

    return lines