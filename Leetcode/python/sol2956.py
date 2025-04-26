

# https://leetcode.com/problems/find-common-elements-between-two-arrays/
class Solution:

    def find_elem(self, arr1:list, set1:set) -> int:
        """
        Compare if the values of the set are in the list and return the number of occurrences.
        """
        rslt: int = 0
        for i in arr1:
            if i  in set1:
                 rslt+=1
        return rslt

    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1:set = set(nums1)
        set_nums2:set = set(nums2)
        rslt_a:int = self.find_elem(nums1, set_nums2)
        rslt_b:int = self.find_elem(nums2, set_nums1)

        return [rslt_a, rslt_b]