# https://leetcode.com/problems/max-pair-sum-in-an-array/description/
class Solution:
    def find_two_greatest(self, arr :list[int]) -> list[int]:
        first = float("-inf")
        second = float("-inf")
        for i in arr:
            if i > first:
                second = first
                first = i
            elif second < i:
                second = i
        return [first, second]

    def maxSum(self, nums: List[int]) -> int:
        dict_max_digit = defaultdict(list)
        for i in nums:
            max_digit = int(max(str(i)))
            dict_max_digit[max_digit].append(i)

        max_sum :int = -1
        for key, arr in dict_max_digit.items():
            if 2 <= len(arr) :
                max_sum = max(max_sum, sum(self.find_two_greatest(arr)))
        return max_sum



