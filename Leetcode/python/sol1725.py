# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        count = 0
        for i in rectangles:
            side = min(i)
            if side > max_len:
                max_len = side
                count = 1
            elif max_len == side:
                count += 1
        return count
        # l = [min(i) for i in rectangles]
        # max_len = max(l)
        # return l.count(max_len)
