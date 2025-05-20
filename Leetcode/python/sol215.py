
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq

class maxHeap:
    def __init__(self):
        self.max_heap = []
    def push(self, val):
        heapq.heappush(self.max_heap, -val)
    def pop(self):
        return -heapq.heappop(self.max_heap)
    def __repr__(self):
        return str([-i for i in self.max_heap])


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return nums[0]
        max_heap = maxHeap()
        for i in nums:
            max_heap.push(i)
        for _ in range(k-1):
            max_heap.pop()
        return max_heap.pop()

