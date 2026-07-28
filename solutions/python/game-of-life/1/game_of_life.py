# import copy

# def count_alive_neighbors(row, column, matrix):
    # having to pass the full matrix here might make this expensive, prohibitively so for large-scale data/..  

def tick(matrix):
    if matrix == []:
        return []
    
    m = [row[:] for row in matrix] # [row.copy() for row in matrix] # copy.deepcopy(matrix) # -> requires import copy # Deep copies: # matrix.copy() # matrix
    rows_count = len(m)
    columns_count = len(m[0])

    def count_alive_neighbors(row, column):
        # count_alive_neighbors = 0 
        return len([(neighbor_row, neighbor_column) 
                    for neighbor_row in range(rows_count)
                        for neighbor_column in range(columns_count)
                            if abs(neighbor_row - row) <= 1 
                                and abs(neighbor_column - column) <= 1
                                and not((neighbor_row, neighbor_column) == (row, column))
                                and matrix[neighbor_row][neighbor_column] == 1
                   ]
                  )
    
    # for row, actual_row in enumerate(matrix):
        # for column, actual_column in enumerate(actual_row):
    for row in range(rows_count):
        for column in range(columns_count):
            alive_neighbors = count_alive_neighbors(row, column)
            if alive_neighbors == 3:
                m[row][column] = 1
                continue
            if matrix[row][column] == 1 and alive_neighbors == 2:
                m[row][column] = 1
                continue
            m[row][column] = 0

    return m