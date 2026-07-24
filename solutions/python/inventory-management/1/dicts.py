"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """

    inventory = {}

    # inventory.add_items(items)
    
    # for current_index, current_item in enumerate(items):
    for current_item in set(items):
        inventory[current_item] = items.count(current_item)

    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    # last_index = len(inventory)

    # for new_item_list_index in range(len(items)): # current_item in items:
       # inventory[last_index + new_item_list_index] = items[new_item_list_index] # current_item

    for new_item in set(items):
        if new_item in inventory:
            inventory[new_item] = inventory[new_item] + items.count(new_item)
        else:
            inventory[new_item] = items.count(new_item)        

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    for decremented_item in set(items):
       # inventory.remove_item(item) # remove_item(inventory, item)
        if decremented_item in inventory:
            inventory[decremented_item] = inventory[decremented_item] - items.count(decremented_item)
            if inventory[decremented_item] < 0:
                inventory[decremented_item] = 0

    return inventory
    

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item) 

    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    inventory_list = [(key, inventory[key]) for key in inventory if inventory[key] > 0] # list(inventory) -> only keys
    
    return inventory_list
