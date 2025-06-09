

# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def set_row_zeros(self, matrix:List[List[int]], row:int) -> None:
        row_to_modified = matrix[row]
        for i in range(len(row_to_modified)):
            row_to_modified[i] = 0

    def set_col_zeros(self, matrix:List[List[int]], col:int) -> None:
        for i in range(len(matrix)):
            matrix[i][col] = 0
    def search_zeros(self, matrix:List[List[int]]) -> tuple:
        elements_to_change = []
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        return (row, col)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #get the original matrix zeros' locations.
        row, col = self. search_zeros(matrix)

        for element in row:
            self.set_row_zeros(matrix, element)
        for element in col:
            self.set_col_zeros(matrix, element)