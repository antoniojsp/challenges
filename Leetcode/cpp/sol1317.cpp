
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/?envType=daily-question&envId=2025-09-08

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        result:list[int] = []
        for i in range(n+1):
            if '0' not in str(i) and '0' not in str(n-i):
                result+= [i, n-i]
                break
        return result
