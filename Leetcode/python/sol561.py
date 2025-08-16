# https://leetcode.com/problems/array-partition/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        rslt = 0
        for i in range(0, len(nums), 2):
            rslt += nums[i]

        return rslt


# slow but N

class Solution:
    def sort_in_n(self, nums:list)->list:
        offset = 10000
        array = [0]*20001 # constraint
        for i in nums:
            array[i+offset]+=1
        result = []
        for i, val in enumerate(array):
            if val > 0:
                for _ in range(val):
                    result.append(i-offset)
        return result

    def arrayPairSum(self, nums: List[int]) -> int:
        arr_sorted = self.sort_in_n(nums)
        rslt = 0
        for i in arr_sorted[::2]:
            rslt+=i

        return rslt

