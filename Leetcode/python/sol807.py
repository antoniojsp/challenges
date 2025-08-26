
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_rows = [max(row) for row in grid] # list of max value per row
        max_col = [max(col) for col in zip(*grid)] # list of max per col
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                limit = min(max_rows[row], max_col[col]) # max height possible without change skyline
                result += limit - grid[row][col]    # sum of differences between the current height and the limit height
        return result
