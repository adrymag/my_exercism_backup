class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        return [int(x) for x in self.matrix_string.split("\n")[index - 1].split(" ")]

    def column(self, index):
        m = [row.split(" ") for row in self.matrix_string.split("\n")]
        print(m)
        # columns_count = len(m[0])
        rows_count = len(m)
        return [int(x) for x in [m[current_rowindex][index-1] for current_rowindex in range(rows_count)]]