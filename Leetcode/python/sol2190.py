# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = defaultdict(int)
        max_freq = float('-inf')
        result = 0
        for i in range(len(nums ) -1):
            if nums[i] == key:
                count[nums[i+1]]+=1
                if max_freq < count[nums[ i +1]]:
                    max_freq = count[nums[ i +1]]
                    result = nums[ i +1]
        return result


