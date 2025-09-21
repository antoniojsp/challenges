
# https://leetcode.com/problems/valid-mountain-array/description/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: # if less than 3
            return False
        if arr[0] > arr[1] or arr[-2] < arr[-1]:
            return False
        start = 0
        end = len(arr) - 1
        l, r = True, True
        while l or r: # look for the point of slope change from both ends.
            if l and arr[start] < arr[start+1]:
                start+=1
            else:
                l = False
            if r and arr[end-1] > arr[end]:
                end-=1
            else:
                r = False
        return start ==  end # if the point of slope change from the start and end is not the same  then there is more than one mountain
