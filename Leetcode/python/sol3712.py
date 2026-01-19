 # https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/description/
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        result = 0
        for val, freq in count.items():
            if freq % k == 0:
                result+=val *freq
        return result
