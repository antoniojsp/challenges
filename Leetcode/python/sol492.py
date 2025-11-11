
# https://leetcode.com/problems/construct-the-rectangle/description/


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        start = int(sqrt(area))
        val = 1
        for i in range(start, 1, -1):
            if area%i == 0:
                val = i
                break
        return [area//val, val]