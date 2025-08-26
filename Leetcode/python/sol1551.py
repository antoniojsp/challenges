
# https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/

class Solution:
    def minOperations(self, n: int) -> int:
        return (n**2)//4
        # arr = [2*i+1 for i in range(n)]
        # return sum(abs(n - i) for i in arr)//2


