
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    Q = []
                    num_islands+=1
                    Q.append((row, col))
                    while Q:
                        x, y = Q.pop()
                        for dx, dy in directions:
                            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x+dx][y+dy] == "1":
                                Q.append((x+dx, y+dy))
                                grid[x+dx][y+dy] = "0"
        return num_islands