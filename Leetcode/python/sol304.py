# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
from pprint import pprint

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0 ] *len(matrix[0]) for i in range(len(matrix))]
        row = len(self.matrix)
        col =  len(self.matrix[0])
        for i in range(row):
            self.matrix[i][0] = matrix[i][0]
            for j in range(1, col):
                self.matrix[i][j] = self.matrix[i][ j -1 ] +matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 +1):
            starting = 0 if col1 == 0 else self.matrix[i][col1 -1]
            total+=(self.matrix[i][col2] - starting)
        return total

# Your NumMatrix object will be instantiated and called as such:.
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            raise ValueError("Empty array")

        self.table = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        # add top row
        for i in range(1, len(self.table[0])):
            self.table[1][i] = self.table[1][i - 1] + matrix[0][i - 1]

        # add first left column
        for i in range(1, len(self.table)):
            self.table[i][1] = self.table[i - 1][1] + matrix[i - 1][0]
            # calculate values by adding up + left - topleft
        for row in range(2, len(self.table)):
            for col in range(2, len(self.table[0])):
                self.table[row][col] = matrix[row - 1][col - 1] + self.table[row][col - 1] + self.table[row - 1][col] - \
                                       self.table[row - 1][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        right_bottom = self.table[row2 + 1][col2 + 1]
        top = self.table[row1][col2 + 1]
        left = self.table[row2 + 1][col1]
        remove = self.table[row1][col1]
        return right_bottom - top - left + remove

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)