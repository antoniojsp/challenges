# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq

class MedianFinder:

    def __init__(self):
        self.arr_low = []
        self.arr_high = []
        self.size = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr_low, -num)  # add first to lower half

        temp = -heapq.heappop(self.arr_low)  # move the greatest in the lowest half to the top half
        heapq.heappush(self.arr_high, temp)

        if len(self.arr_low) < len(self.arr_high):
            heapq.heappush(self.arr_low, -heapq.heappop(self.arr_high))
        self.size += 1

    def findMedian(self) -> float:
        rslt = 0
        if self.size % 2 == 0:
            bottom_top = -self.arr_low[0]
            top_bottom = self.arr_high[0]
            rslt = (bottom_top + top_bottom) / 2
        else:
            if len(self.arr_low) < len(self.arr_high):
                rslt = self.arr_high[0]
            else:
                rslt = -self.arr_low[0]

        return rslt

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()




