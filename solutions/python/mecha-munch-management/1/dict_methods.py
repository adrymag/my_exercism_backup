"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    # Create a shallow copy of the current cart so we don't mutate the
    # original dictionary passed in by the caller.
    updated_cart = current_cart.copy()

    # Iterate over every item in the items_to_add iterable.
    # The iterable could be a tuple, list, or any other sequence.
    for item in items_to_add:
        # dict.get(key, default) retrieves the current quantity for this item.
        # If the item is not yet in the cart, get() returns 0 (the default).
        # We then add 1 to that value and assign it back to the key,
        # either incrementing an existing item or adding a new one with qty 1.
        updated_cart[item] = updated_cart.get(item, 0) + 1

    return updated_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    # dict.fromkeys(iterable, value) creates a new dictionary using each
    # element of the iterable as a key, all mapped to the same value.
    # Here we map every item to a quantity of 1. Duplicate items in the
    # iterable are naturally collapsed into a single key because dict
    # keys must be unique.
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    # Make a copy of the existing ideas dictionary so the original is
    # not modified in-place.
    updated_ideas = ideas.copy()

    # recipe_updates is an iterable of (recipe_name, ingredients_dict) pairs.
    # We unpack each pair and assign the new ingredients dict to the recipe
    # name. This replaces an existing recipe entirely or adds a brand-new one.
    for recipe_name, ingredients in recipe_updates:
        updated_ideas[recipe_name] = ingredients

    return updated_ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    # cart.items() yields (key, value) tuples.
    # sorted() arranges these tuples by the first element (the key) in
    # ascending alphabetical order by default.
    # Passing the result to dict() reconstructs a new dictionary with
    # the sorted order preserved (Python 3.7+).
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    # Build a new dictionary that combines quantity with store metadata.
    fulfillment_cart = {}

    # Walk through each item and its quantity in the user's cart.
    for item, quantity in cart.items():
        # aisle_mapping stores a list like ['Aisle 4', False] for each item.
        # We unpack that list into the aisle string and refrigeration bool.
        aisle, refrigeration = aisle_mapping[item]

        # Store the combined data as a single list: [qty, aisle, refrigeration].
        fulfillment_cart[item] = [quantity, aisle, refrigeration]

    # Return the fulfillment cart sorted in reverse alphabetical order.
    # sorted(..., reverse=True) sorts the (key, value) tuples by key
    # in descending order. dict() then rebuilds the ordered mapping.
    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    # Prepare a new dictionary to hold the updated inventory without
    # mutating the original store_inventory lists in-place.
    updated_inventory = {}

    # Iterate over the store inventory so we preserve its structure and
    # key order. Each value is a list like [count, 'Aisle 5', False].
    for item, details in store_inventory.items():
        # Make a shallow copy of the details list so we don't modify
        # the original store_inventory data.
        updated_details = list(details)

        # If this item appears in the fulfillment cart, subtract the
        # ordered quantity from the current stock count.
        if item in fulfillment_cart:
            ordered_quantity = fulfillment_cart[item][0]
            new_count = updated_details[0] - ordered_quantity

            # When stock falls to 0 (or below), replace the numeric count
            # with the string 'Out of Stock' per the requirements.
            if new_count <= 0:
                updated_details[0] = 'Out of Stock'
            else:
                updated_details[0] = new_count

        # Add the (possibly modified) details to the new inventory dict.
        updated_inventory[item] = updated_details

    return updated_inventory