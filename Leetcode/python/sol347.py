# https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =  Counter(nums)
        freq :list[list[int]] = [[] for i in range(len(nums ) +1)]
        for num, times in count.items():
            freq[times].append(num)

        rslt :list[int] = []
        for i in freq[::-1]:
            if i:
                rslt.extend(i)

        return rslt[:k]




