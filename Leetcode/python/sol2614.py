# https://leetcode.com/problems/prime-in-diagonal/solutions/7198757/easy-by-antoniojsp-nuz0/
class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        if n in {2 ,3}:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        for i in range(5, int(sqrt(n) ) +1, 6):
            if n% i == 0 or n % (i + 2) == 0:
                return False
        return True

    def check_top_left_max(self, nums):
        maximum = 0
        x, y = 0, 0
        for i in range(len(nums)):
            if self.is_prime(nums[x][y]):
                maximum = max(nums[x][y], maximum)
            x += 1
            y += 1
        return maximum

    def check_top_right_max(self, nums):
        maximum = 0
        x, y = 0, len(nums) - 1
        for i in range(len(nums)):
            if self.is_prime(nums[x][y]):
                maximum = max(nums[x][y], maximum)
            x += 1
            y -= 1
        return maximum

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        return max(self.check_top_left_max(nums), self.check_top_right_max(nums))

