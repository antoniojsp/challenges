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

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)