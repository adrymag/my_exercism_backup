"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_numbers):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return [x for x in wagon_numbers]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    return [1] + missing_wagons + each_wagons_id[3:] + each_wagons_id[0:2]


def add_missing_stops(*route, **stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.

    Sample call: print(add_missing_stops({"from": "New York", "to": "Miami"},
                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                      stop_4="Jacksonville", stop_5="Orlando"))

    Sample output (for that call): {"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}

    """

    # print(stops) # {'stop_1': 'Washington, DC', 'stop_2': 'Charlotte', 'stop_3': 'Atlanta', 'stop_4': 'Jacksonville', 'stop_5': 'Orlando'}

    # stops_list = '"'

    # for (stop_key, stop_value) in stops.items():
    #     stops_list += stop_value + '", "'

    # stops_list = stops_list[:-3]

    # stops_list = '"' + '", "'.join(stops.values()) + '"'
    # print(stops_list)

    # print(stops.values()) # dict_values(['Washington, DC', 'Charlotte', 'Atlanta', 'Jacksonville', 'Orlando'])

    # print(list(stops.values()))

    # route["stops"] = list(stops.values()) # stops.values() # TypeError: 'tuple' object does not support item assignment

    new_route = {}

    new_route["from"] = route[0]["from"] # TypeError: tuple indices must be integers or slices, not str
    new_route["to"] = route[0]["to"]
    new_route["stops"] = list(stops.values())

    return new_route # route + { "stops": stops.values() }


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """

    for (key, value) in more_route_information.items():
        route[key] = value

    # for item in more_route_information.items():
        # (key, value) = item
        # route[key] = value # route.insert(item) # .add
    
    return route # route.extend(more_route_information) # route + more_route_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """

    [row1, row2, row3] = wagons_rows
    [t11, t12, t13] = row1
    [t21, t22, t23] = row2
    [t31, t32, t33] = row3

    new_row1 = [t11, t21, t31]
    new_row2 = [t12, t22, t32]
    new_row3 = [t13, t23, t33]

    new_wagons_rows = [new_row1, new_row2, new_row3]
    
    return new_wagons_rows
