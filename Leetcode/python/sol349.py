# https://leetcode.com/problems/intersection-of-two-arrays/description/
from collections import defaultdict, Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)
        # version 2
        # all_values = list(set(nums1)) + list(set(nums2))
        # count = Counter(all_values)
        # result = []
        # for val, freq in count.items():
        #     if freq > 1:
        #         result.append(val)
        # return result
        # version 2
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # counter = defaultdict(int)
        # for i in nums1_set:
        #     counter[i]+=1
        # for i in nums2_set:
        #     counter[i]+=1
        # return [i for i, j in counter.items() if j > 1]
