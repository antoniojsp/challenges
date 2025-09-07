
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/

from collections import defaultdict
class Solution:
    def sum_digits(self, n:int) -> int:
        result = 0
        while n:
            result+=n%10
            n//=10
        return result

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            val = self.sum_digits(i)
            count[val]+=1
        return max(count.values())