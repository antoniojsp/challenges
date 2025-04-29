# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/?envType=problem-list-v2&envId=sorting



class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counting = list(Counter(nums).items())
        counting.sort(key=lambda x:x[0], reverse=True)
        counting.sort(key=lambda x:x[1])
        result = []
        for i, j in counting:
            result.extend([i]*j)
        return result



