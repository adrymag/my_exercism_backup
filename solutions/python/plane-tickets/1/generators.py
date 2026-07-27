"""Functions to automate Conda airlines ticketing system."""
import math

SEATS_IN_ROW = ['A', 'B', 'C', 'D']

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    for seat in range(number):
        yield SEATS_IN_ROW[seat % 4]
    # return 


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    for seat in range(number):
        if seat > 47 : # if int(seat/4) + 1 >= 13:
            seat += 4
        yield str(int(seat/4) + 1) + SEATS_IN_ROW[seat % 4]
    # pass


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = {}
    passengers_count = len(passengers)
    seats_list = list(generate_seats(passengers_count))

    for current_passenger_count in range(passengers_count):
        seats[passengers[current_passenger_count]] = seats_list[current_passenger_count]
    
    return seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers: # ["12A", "38B", "69C", "102B"]
        yield seat + flight_id + (12 - len(seat) - len(flight_id)) * "0"