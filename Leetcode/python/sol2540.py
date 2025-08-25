# https://leetcode.com/problems/minimum-common-value/description/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif  nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return -1

        # using sets
        # common_elements = set(nums1) & set(nums2)
        # return min(common_elements) if common_elements else -1