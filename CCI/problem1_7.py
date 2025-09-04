import unittest

test_cases = [
    # 1x1 matrix
    ([[1]], [[1]]),

    # 2x2 matrix
    ([[1, 2],
      [3, 4]],
     [[3, 1],
      [4, 2]]),

    # 3x3 matrix
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     [[7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]]),

    # 4x4 matrix
    ([[ 1,  2,  3,  4],
      [ 5,  6,  7,  8],
      [ 9, 10, 11, 12],
      [13, 14, 15, 16]],
     [[13,  9,  5, 1],
      [14, 10,  6, 2],
      [15, 11,  7, 3],
      [16, 12,  8, 4]]),

    # Empty matrix
    ([], []),
]

def rotate_matrix(matrix):
    if not matrix:
        return matrix
    result = []
    for col in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)-1, -1, -1):
            temp.append(matrix[row][col])
        result.append(temp)
    return result

# print(rotate_matrix(test_cases[1][0]))

class TestRotateMatrix(unittest.TestCase):
    def test_rotate(self):
        for matrix, expected in test_cases:
            with self.subTest(matrix=matrix):
                self.assertEqual(rotate_matrix([row[:] for row in matrix]), expected)

if __name__ == "__main__":
    unittest.main()
