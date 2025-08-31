# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts] # convert too negative to use a max-heap
        heapq.heapify(gifts)
        for _ in range(k):
            top = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(sqrt(top)))
        return sum(-i for i in gifts)
