
# https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [i for i in nums if i%2==0] # filter evens
        freq = list(Counter(even).items()) # count frequencies
        result = sorted(freq, key=lambda x: (-x[1], x[0])) # sorts
        return result[0][0] if result else -1
