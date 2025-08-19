
# https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [i for i in nums if i%2==0] # filter evens
        freq = list(Counter(even).items()) # count frequencies
        result = sorted(freq, key=lambda x: (-x[1], x[0])) # sorts
        return result[0][0] if result else -1


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = list(Counter(i for i in nums if i%2==0).items()) # count frequencies
        max_freq = -1
        for i in freq:
            max_freq = max(max_freq, i[1])
        values_max_freq = [(i, j) for i, j in freq if j == max_freq]
        min_val = float('inf')
        for i in values_max_freq:
            min_val = min(min_val, i[0])
        return min_val if min_val != float('inf') else -1