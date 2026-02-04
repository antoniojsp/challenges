# https://leetcode.com/problems/map-of-highest-peak/

from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        Q = deque()
        rows, cols = len(isWater), len(isWater[0])
        heights = [[float(-1)] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    Q.append((i, j))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while Q:
            r, c = Q.popleft()
            for dr, dc in directions:
                n_row = r + dr
                n_col = c + dc
                if 0 <= n_row < rows and 0 <= n_col < cols:
                    if heights[n_row][n_col] == -1:
                        heights[n_row][n_col] = heights[r][c] + 1
                        Q.append([n_row, n_col])

        return heights
