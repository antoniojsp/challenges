# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        sequence = []
        def dfs(curr):
            if len(sequence) == k:
                res.append(sequence[:])
                return

            need = k - len(sequence)

            for i in range(curr,  n - need + 2):
                sequence.append(i)
                dfs( i +1)
                sequence.pop()

        dfs(1)
        return res

