class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {}
        for idx, val in enumerate(nums2):
            index[val] = idx
        result = []

        for i in nums1:
            pos = index[i]
            curr_max = -1
            if nums2[pos + 1:]:
                for j in nums2[pos + 1:]:
                    if i < j:
                        curr_max = j
                        break
            result.append(curr_max)
        return result





