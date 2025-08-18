# https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/
class Solution:
    def check_left(self, grid )->bool:
        row, col = 0, 0
        while row < len(grid) and col < len(grid[0]):
            if grid[row][col] == 0:
                return False
            else:
                grid[row][col] = -1
            row+=1
            col+=1
        return True

    def check_right(self, grid )->bool:
        row, col = 0, len(grid[0] ) -1
        while row < len(grid) and 0 <= col:
            if grid[row][col] == 0:
                return False
            else:
                grid[row][col] = -1
            row+=1
            col-=1
        return True

    def check_all(self, grid):

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0 and grid[row][col] != -1:
                    return False
        return True

    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        return self.check_left(grid) and self.check_right(grid) and self.check_all(grid)



class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if (i == j or i + j == n - 1): # diagonal
                    if grid[i][j] == 0:
                        return False
                else:  # non diagonal
                    if grid[i][j] != 0:
                        return False
        return True
