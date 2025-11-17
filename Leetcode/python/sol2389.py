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


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]
        result = []
        for q in queries:
            count = 0
            for n in nums:
                if n <= q:
                    count+=1
                else:
                    break
            result.append(count)
        return result
