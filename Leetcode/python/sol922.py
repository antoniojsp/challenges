# https://leetcode.com/problems/sort-array-by-parity-ii/description/
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [i for i in nums if i% 2 != 0]
        even = [i for i in nums if i % 2 == 0]
        ans = []

        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(even.pop())
            else:
                ans.append(odd.pop())
        return ans

