
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rslt = [-1] # keep track of the greatest while looping right to left.

        for val in arr[:0:-1]: # loop from the end of the arr to the element in place 1.
            if val > rslt[-1]: # if current value is grater than the last element in rslt, then add the value to rslt (last element is considered the current greatests)
                rslt.append(val)
            else: #if last element from rslt is not greater, add again that value to the rslt
                rslt.append(rslt[-1])

        return rslt[::-1] # inverse the rslt list