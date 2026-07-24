"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    return tuple(coordinate) # (coordinate[0], coordinate[1]) # list(coordinate) -> not working, returns a list, not a tuple


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """

    if rui_record[1] == tuple(azara_record[1]):
        return True

    return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if rui_record[1] == tuple(azara_record[1]):
        return tuple([azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2]])

    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """

    report = "" # '"""'
    for current_combined_record_no, current_combined_record in enumerate(combined_record_group):
        cleaned_combined_record_group = ["'" + current_combined_record[0] + "'", "'" + current_combined_record[2] + "'", str(current_combined_record[3]), "'" + current_combined_record[4] + "'"]
        # print("CCRG:")
        # print(cleaned_combined_record_group)
        
        # report = report + "(" + "', '".join(cleaned_combined_record_group) + ")\n"
        report = report + "(" + ", ".join(cleaned_combined_record_group) + ")\n" # + ")\\n"
        # if current_combined_record_no == len(combined_record_group) - 1:
        #     report = report + '"""'
        # else:
        #     report = report + "\\\n"

    return report