# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution:
    def max_len_subsequence(self, nums:list, suma:int) -> int:
        length = 0
        for i in nums:
            if suma - i >= 0:
                length+=1
                suma -=i
        return length

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        return [self.max_len_subsequence(nums, i) for i  in queries]