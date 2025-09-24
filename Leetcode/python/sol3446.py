
# https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution:
    def traverse_diagonal(self, grid, x, y, is_reversed):
        diagonal = []
        n = len(grid)
        i = 0
        while x+i < n and y+i < n: # extract the values from the diagonal
            diagonal.append(grid[x+i][y+i])
            i+=1

        diagonal.sort(reverse=is_reversed) # depends if it's top or lower triangle, sort
        for idx, val in enumerate(diagonal):
            grid[x+idx][y+idx] = val


    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        x = 0 # start from the top and go down (to check lower triangle)
        for i in range(len(grid)):
            self.traverse_diagonal(grid, x+i, 0, is_reversed=True)
        y = 1 # start to the right of the middle diagonal to check top triangle
        for i in range(len(grid)):
            self.traverse_diagonal(grid, 0, y+i, is_reversed=False)
        return grid