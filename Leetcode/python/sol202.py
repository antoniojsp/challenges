# https://leetcode.com/problems/happy-number/description/
class Solution:

    def separate(self, num :int) -> list[int]:
        rslt :list = []
        while 1<= num:
            rslt.append(num % 10)
            num //= 10
        return rslt

    def square_sum(self, arr: list[int]) -> int:
        rslt: int = 0
        for i in arr:
            rslt += i ** 2
        return rslt

    def isHappy(self, n: int) -> bool:
        seen: set = set()
        while True:
            seen.add(n)
            n = self.square_sum(self.separate(n))
            if n == 1:
                return True
            elif n in seen:
                return False

        return False
