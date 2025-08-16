# https://leetcode.com/problems/two-out-of-three/description/
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = {}
        for group in [nums1, nums2, nums3]:
            temp = set(group)
            for i in temp:
                freq[i] = freq.get(i, 0 ) +1

        return [i for i, v in freq.items() if v > 1]