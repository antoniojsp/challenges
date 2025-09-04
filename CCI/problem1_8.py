import unittest

test_cases = [
    ([[0]], [[0]]),                       # 1x1 zero
    ([[5]], [[5]]),                       # 1x1 non-zero
    ([[1, 0], [3, 4]], [[0, 0], [3, 0]]), # 2x2 single zero
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]), # 2x2 no zero

    ([[1, 2, 3], [4, 0, 6], [7, 8, 9]],   # 3x3 zero in middle
     [[1, 0, 3], [0, 0, 0], [7, 0, 9]]),

    ([[0, 2, 0], [4, 5, 6], [7, 8, 9]],   # zeros in corners
     [[0, 0, 0], [0, 5, 0], [0, 8, 0]]),
    ([[1, 2, 0, 4], [5, 6, 7, 8],           # 4x4 multiple zeros
      [9, 0, 11, 12], [13, 14, 15, 16]],
     [[0, 0, 0, 0], [5, 0, 0, 8], [0, 0, 0, 0], [13, 0, 0, 16]]),
    ([], []),                               # empty matrix
    ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),   # all zeros
    ([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]), # no zeros
]

class ZeroMatrix:
    # Function to implement
    def set_col_zero(self, matrix, col):
        for row in range(len(matrix)):
            matrix[row][col] = 0

    def set_row_zero(self, matrix, row):
        for col in range(len(matrix[0])):
            matrix[row][col] = 0

    def zero_matrix(self, matrix):
        points = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    points.append((row, col))
        for row, col in points:
            self.set_col_zero(matrix, col)
            self.set_row_zero(matrix, row)
        return matrix




class TestZeroMatrix(unittest.TestCase):
    def test_zero_matrix(self):
        for matrix, expected in test_cases:
            with self.subTest(matrix=matrix):
                # Copy matrix to avoid modifying test cases
                input_copy = [row[:] for row in matrix]
                ZeroMatrix().zero_matrix(input_copy)
                self.assertEqual(input_copy, expected)

if __name__ == "__main__":
    unittest.main()



