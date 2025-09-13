# https://leetcode.com/problems/find-champion-i/description/


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        winner = 0 # set up the first team as winner by default
        max_num_weaker = sum(grid[0]) # number of teams that team zero is superior
        for i, teams in enumerate(grid[1:], start=1):
            temp = sum(teams)
            if max_num_weaker < temp:
                winner = i
                max_num_weaker = temp
        return winner

