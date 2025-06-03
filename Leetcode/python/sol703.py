#  https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        heapq.heapify(self.arr)
        self.kth = k

    def check_size(self) -> None:
        while len(self.arr) > self.kth:
            heapq.heappop(self.arr)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        self.check_size()
        return self.arr[0]

# 4 5 8     2 4 5 8
# 3 4 5     2 3 4 5 8
# 4 5 5     2 3 4 5 5 8
# 5 5 10    2 3 4 5 5 8 10
# 5 9 10    2 3 4 5 5 8 9 10
# 4 9 10    2 3 4 4 5 5 8 10




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)