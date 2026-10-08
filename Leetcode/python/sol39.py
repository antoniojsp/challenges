# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        sequence = []
        def dfs(start, curr):
            if curr == 0:
                res.append(sequence[:])
                return

            if curr < 0:
                return

            for i in range(start, len(candidates)):
                sequence.append(candidates[i])
                dfs(i, curr - candidates[i])
                sequence.pop()

        dfs(0, target)
        return res

