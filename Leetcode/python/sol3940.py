# https://leetcode.com/problems/limit-occurrences-in-sorted-array/description/

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

                candidate = candidates[i]
                if candidate > curr:
                    break
                sequence.append(candidate)
                dfs(i, curr - candidate)
                sequence.pop()

        dfs(0, target)
        return res

