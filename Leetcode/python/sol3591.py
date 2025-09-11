# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/
class Solution:
    def check_prime(self, num :int):
        if num <= 1:
            return False
        if num == 2:
            return True
        if nu m %2 ==  0:
            return False

        root = int(sqrt(num))
        for i in range(3 ,roo t +1, 2):
            if nu m %i == 0:
                return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        count = set(Counter(nums).values())
        print(count)
        return any(self.check_prime(i) for i in count)
