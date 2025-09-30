

# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def sort_diagonal(self, grid, row, col) -> None:
        i, j = row, col
        diagonal = []
        while i < len(grid) and j < len(grid[0]):
            diagonal.append(grid[i][j])
            i+=1
            j+=1

        diagonal.sort()

        i, j = row, col
        for val in diagonal:
            grid[i][j] = val
            i+=1
            j+=1

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(0, len(mat[0])):
            self.sort_diagonal(mat, 0, i)

        for i in range(1, len(mat)): # start from 1 since the previos loop already took care of (0,0)
            self.sort_diagonal(mat, i,0)

        return mat