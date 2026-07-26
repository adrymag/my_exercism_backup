def get_maximum_value(list):
    """get_maximum_value_from_list"""

    maximum_value = None

    # maximum_value = list[0]    
    # maximum_positions = {0} # position = 0

    maximum_positions = set()

    for position, value in enumerate(list):
        if maximum_value == None:
            [maximum_position, maximum_value] = [position, value]
            pass
        if value > maximum_value:
            # [maximum_position, maximum_value] = [position, value]
            maximum_positions = {position}
            maximum_value = value
        elif value == maximum_value:
            maximum_positions.add(position)
        
    return [maximum_positions, maximum_value]

def update_column_minimum_values(minimum_column_values, all_minimum_column_positions, current_line, current_line_number, total_columns_number):
    for current_column_number in range(total_columns_number):
        if current_line[current_column_number] < minimum_column_values[current_column_number]:
            minimum_column_values[current_column_number] = current_line[current_column_number]
            all_minimum_column_positions[current_column_number] = {current_line_number}
        elif current_line[current_column_number] == minimum_column_values[current_column_number]:
            all_minimum_column_positions[current_column_number].add(current_line_number)

    return [minimum_column_values, all_minimum_column_positions]

def saddle_points(matrix):
    if matrix == None or len(matrix) == 0 or matrix == [] or matrix == [[]]:
        return []

    total_lines_number = len(matrix)
    total_columns_number = len(matrix[0])

    for current_line_number in range(total_lines_number):
        current_line = matrix[current_line_number]
        if len(current_line) != total_columns_number:
            # if the matrix is irregular
            raise ValueError("irregular matrix")

    if total_lines_number == 1: # print("test")
        [maximum_positions, maximum_value] = get_maximum_value(matrix[0])
        print([maximum_positions, maximum_value])
        saddle_points_positions = [] # [{1, 3}, 5] # [{'row': 1, 'column': 2}, {'row': 1, 'column': 4}]
        for current_column_number in maximum_positions:
            current_saddle_point_record = {}
            current_saddle_point_record['row'] = 1
            current_saddle_point_record['column'] = current_column_number + 1
            saddle_points_positions.append(current_saddle_point_record)
        return saddle_points_positions

    if total_columns_number == 1: # print("test")
        minimum_positions = {}
        minimum_value = matrix[0][0]
        for current_line_number in range(1, total_lines_number):
            if matrix[current_line_number][0] < minimum_value:
                minimum_positions = {current_line_number}
                minimum_value = matrix[current_line_number][0]
            elif matrix[current_line_number][0] == minimum_value:
                minimum_positions.add(current_line_number)
        saddle_points_positions = []
        for current_line_number in minimum_positions:
            current_saddle_point_record = {}
            current_saddle_point_record['row'] = current_line_number + 1
            current_saddle_point_record['column'] = 1
            saddle_points_positions.append(current_saddle_point_record)
        return saddle_points_positions

    all_maximum_line_positions_set = set()
    # all_minimum_column_positions_set = set()
    all_maximum_line_positions = list(range(total_lines_number))
    all_minimum_column_positions = {} # list(range(total_lines_number))

    for current_column_number in range(total_columns_number):
        minimum_column_values = matrix[0] # first_line
        # all_minimum_column_positions_set.add((0, current_column_number))
        all_minimum_column_positions[current_column_number] = {0}

    for current_line_number in range(total_lines_number):
        current_line = matrix[current_line_number]

        if current_line_number > 0:
            [minimum_column_values, all_minimum_column_positions] = update_column_minimum_values(minimum_column_values, all_minimum_column_positions, current_line, current_line_number, total_columns_number) # update_column_minimum_values
        
        [maximum_positions, maximum_value] = get_maximum_value(current_line)
        all_maximum_line_positions[current_line_number] = maximum_positions

        # print(f"Line no. {current_line_number} :",  )
        # print(current_line)
        # print([maximum_positions, maximum_value])

        for current_line_maximum_position in maximum_positions:
            all_maximum_line_positions_set.add((current_line_number, current_line_maximum_position))

    # print(all_maximum_line_positions_set)
    # print(all_maximum_line_positions)
    # print(minimum_column_values)
    # print(all_minimum_column_positions)

    saddle_points_positions = []

    for current_line_number in range(total_lines_number):
        for line_maximum_column_position in all_maximum_line_positions[current_line_number]:
            if current_line_number in all_minimum_column_positions[line_maximum_column_position]:
                # saddle_points_positions.append((current_line_number, line_maximum_column_position))
                # saddle_points_positions.append(("'row': " + str(current_line_number + 1), "'column': " + str(line_maximum_column_position + 1)))
                current_saddle_point_record = {}
                current_saddle_point_record['row'] = current_line_number + 1
                current_saddle_point_record['column'] = line_maximum_column_position + 1
                saddle_points_positions.append(current_saddle_point_record)

    return saddle_points_positions # [{'row': 2, 'column': 1}] # [(1, 0)] [{'row': 2, 'column': 1}] # [{'row': 2, 'column': 1}] # [{'column': 1, 'row': 2}]