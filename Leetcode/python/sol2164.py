

# https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
class Solution:
    def count_sort(self, nums):
        arr = [0]*(max(nums)+1)
        for i in nums:
            arr[i] += 1
        rslt = []
        for i in range(len(arr)):
            if arr[i] > 0:
                rslt.extend([i]*arr[i])
        return rslt

    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) < 3: # catch cases the array is empy or has 1 or 2 elemets
            return nums
        even = self.count_sort([nums[i] for i in range(len(nums)) if i%2 == 0])
        odd = self.count_sort([nums[i] for i in range(len(nums)) if i%2 != 0])
        e = 0
        o = len(odd)-1
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = even[e]
                e+=1
            else:
                nums[i] = odd[o]
                o-=1
        return nums
