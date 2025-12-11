# https://leetcode.com/problems/range-addition-ii/

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        result = 1
        for val in zip(*ops):
            result*=min(val)
        return result