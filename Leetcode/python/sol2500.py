# https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort(reverse=True)

        suma = 0
        for i in zip(*grid):
            suma += max(i)
        return suma