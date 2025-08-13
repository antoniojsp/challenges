# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/solutions/7076229/brute-force-by-antoniojsp-jetm/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i*j % k == 0:
                    count+=1
        return count


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indexes = defaultdict(list)
        for idx, val in enumerate(nums):
            indexes[val].append(idx)
        count = 0

        # values in each key represent equal values
        # dict keeps the order
        for arr_index in indexes.values():
            for i in range(0, len(arr_index)):
                for j in range(i+1, len(arr_index)):
                    if (arr_index[i]*arr_index[j])%k==0:
                        count += 1
        return count