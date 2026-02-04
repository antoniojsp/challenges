#https://leetcode.com/problems/rotting-oranges/
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = deque()
        rows, cols =  len(grid), len(grid[0])
        distances = [[float('inf')] * cols for _ in range(rows)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    distances[row][col] = 0
                    Q.append((row, col))
        directions = [(0 ,1), (1 ,0), (-1 ,0), (0 ,-1)]
        while Q:
            row, col = Q.popleft() # curr
            for r, c in directions:
                nr = row + r
                nc = col + c
                if 0 <= nr < rows and 0 <= nc < cols: # check bounds
                    if grid[nr][nc] == 1 and distances[nr][nc] > distances[row][col] + 1:
                        distances[nr][nc] = distances[row][col] + 1
                        Q.append((nr, nc))

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and distances[i][j] == float('inf'):
                    return -1
                if grid[i][j] == 1:
                    result = max(result, distances[i][j])
        return result


