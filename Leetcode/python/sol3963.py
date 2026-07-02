
# https://leetcode.com/problems/create-grid-with-exactly-one-path/description/

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        maze = [["#"]*n for _ in range(m)]
        maze[0] = ["."]*n
        for i in range(m):
            maze[i][n-1] = "."
        return ["".join(i) for i in maze]