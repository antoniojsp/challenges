

#https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
class Solution:

    def priority(self, arr:list)->tuple:
        order = []
        for i, j in enumerate(arr):
            order.append((i,j))
        order.sort(key=lambda x:x[1])
        return order

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            tuples = self.priority(nums)
            index, value = tuples[0]
            nums[index] = multiplier*value


        return nums