class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        """Returns the row with the current (currently given) (1-based) index from the matrix

        Parameters:
        self (obj): The current matrix(representation) object.
        index (int): The (1-based) index of the row to extract.

        Returns:
            list(int): The row to extract (with the given 1-based index).
        """
        return [int(x) for x in self.matrix_string.split("\n")[index - 1].split(" ")]

    def column(self, index):
        """Returns the column with the current (currently given) (1-based) index from the matrix

        Parameters:
        self (obj): The current matrix(representation) object.
        index (int): The (1-based) index of the column to extract.

        Returns:
            list(int): The column to extract (with the given 1-based index).
        """
        m = [row.split(" ") for row in self.matrix_string.split("\n")]
        rows_count = len(m) # columns_count = len(m[0])
        return [int(x) for x in [m[current_rowindex][index-1] for current_rowindex in range(rows_count)]]