# https://leetcode.com/problems/combination-sum-ii/description/
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
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

                if i > start and candidate == candidates[ i -1]:
                    continue

                sequence.append(candidate)
                dfs( i +1, curr - candidate)
                sequence.pop()
        dfs(0, target)
        return res
