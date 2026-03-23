# https://leetcode.com/problems/flip-square-submatrix-vertically/?envType=daily-question&envId=2026-03-21

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top = x
        bottom = x+k-1
        while top < bottom:
            for i in range(y, y+k):
                grid[top][i], grid[bottom][i]  = grid[bottom][i], grid[top][i]
            top+=1
            bottom-=1
        return grid


