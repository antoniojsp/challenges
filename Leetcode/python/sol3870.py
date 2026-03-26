

# https://leetcode.com/problems/count-commas-in-range/description/

class Solution:
    def countCommas(self, n: int) -> int:
        # count = 0
        # for i in range(1000, n+1):
        #     if i >= 1000:
        #         count+=1
        # return count
        return 0 if n < 1000 else n - 1000 + 1