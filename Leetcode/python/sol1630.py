# https://leetcode.com/problems/arithmetic-subarrays/
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i, j in zip(l, r):
            list_range = nums[i: j +1][:]
            list_range.sort()
            diff = None
            rslt = True
            for idx in range(len(list_range ) -1):
                diff_curr = list_range[idx] - list_range[id x +1]
                if diff is None:
                    diff = diff_curr
                elif diff != diff_curr:
                    rslt = False
                    break

            result.append(rslt)

        return result

