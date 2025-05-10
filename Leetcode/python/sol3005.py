#  https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def count(self, arr :list[int]) -> dict[int, int]:
        counter :dict[int ,int] = {}
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        return counter

    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter :list[int] = list(self.count(nums).values())
        max_freq :int = max(counter)
        return sum(i for i in counter if i ==  max_freq)


