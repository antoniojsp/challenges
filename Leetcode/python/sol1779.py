
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/


class Solution:
    def nearestValidPoint(self, x: int, y: int, points):
        index_max = -1
        max_distance = float('inf')
        for idx, (x1, y1) in enumerate(points):
            if x1 == x or y1 == y:
                distance = abs(x-x1)+abs(y-y1)
                if distance < max_distance: # we dont use "<=" so only records the first minimum value that is found, in case there are several equal min value
                    max_distance = distance
                    index_max = idx
        return index_max
