import collections
import unittest

class MyMatrix:
    def __init__(self, matrix, rotations):
        self.original_matrix = matrix
        self.rotations = rotations
        self.rotated_matrix = matrix
        self.rotate(self.original_matrix)

    def rotate(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        if rows == 0:
            return

        path_length = len(matrix[0]) * len(matrix)
        rows_generator = self.rows_gen(rows, columns)
        columns_generator = self.columns_gen(rows, columns)
        path = zip(rows_generator, columns_generator)
        print(list(path))

    def path_gen(self, first_row, first_col):
        start = (first_row, first_col)
        current = start
        current_row = first_row
        current_col = first_col
        matrix_height = len(self.rotated_matrix) - 1
        matrix_width = len(self.rotated_matrix[0]) - 1
        while current != start:
            coord = collections.namedtuple('coord', 'row col' )
            top_left = coord(current_row, current_col)
            bottom_left = coord(matrix_height - current_row, current_col)
            bottom_right = coord(matrix_height - current_row, matrix_width - current_col)
            top_right = coord(current_row)
            # down
            for row in range(len(self.rotated_matrix))[current_row:len(self.rotated_matrix) - current_row]:
                if row >
            # right

            # up

            # left


class TestMyMatris(unittest.TestCase):
    def test_rotation(self):
        self.assertEqual([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
                MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4).rotated_matrix)


if __name__ == "__main__":
    unittest.main()




