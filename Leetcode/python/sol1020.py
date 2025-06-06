# https://leetcode.com/problems/number-of-enclaves/description/
from collections import defaultdict
class Solution:
    def check_borders(self, grid):
        exclude = set()
        cols = len(grid[0])
        rows = len(grid)
        # top and botton
        for i in range(cols):
            if grid[0][i] == 1:
                exclude.add((0, i))
            if grid[rows-1][i] == 1:
                exclude.add((rows-1, i))
        # left and right
        for i in range(rows):
            if grid[i][0] == 1:
                exclude.add((i ,0))
            if grid[i][cols-1] == 1:
                exclude.add((i ,cols -1))

        return exclude

    def count_ones(self, grid) -> int:
        result = 0
        for row in grid:
            for element in row:
                result +=element
        return result

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        excluded_border = self.check_borders(grid)
        for source in excluded_border:
            S = [source]
            while S:
                row, col = S.pop()
                if grid[row][col] == 1:
                    # left
                    if 0 < col -1:
                        S.append((row, col -1))
                    # right
                    if col +1 < cols -1:
                        S.append((row, col +1))
                    # upper
                    if 0 < row -1:
                        S.append((row -1, col))
                    # lower
                    if row +1 < rows -1:
                        S.append((row +1, col))
                grid[row][col] = 0

        return self.count_ones(grid)

