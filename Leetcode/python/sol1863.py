
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

from itertools import combinations
class Solution:
    def xor_list(self, arr:list) -> int:
        '''
        Takes a list and return the xor of all the elements
        '''
        return reduce(lambda x, y: x ^ y, arr)

    def subsetXORSum(self, nums: List[int]) -> int:
        sum_xor = 0
        for i in range(1, len(nums)+1):


                sum_xor += self.xor_list(subset)
        print(self.xor_list([5,1,6]))
        return sum_xor
