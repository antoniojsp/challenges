# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/
class Solution:
    def is_odd(self, num :int) -> bool:
        return num % 2 != 0

    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        matrix = [[0 ] *n for i in range(m)]
        for row, col in indices:
            for i in range(len(matrix[row])):
                matrix[row][i] += 1
            for i in range(len(matrix)):
                matrix[i][col] += 1

        rslt = 0
        for row in matrix:
            for val in row:
                if self.is_odd(val):
                    rslt+=1

        return rslt
