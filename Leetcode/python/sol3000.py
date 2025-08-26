# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0
        for l, w in dimensions:
            diagonal = sqrt(l**2 + w**2)
            if max_diagonal < diagonal:
                max_diagonal = diagonal
                max_area = l* w
            elif max_diagonal == diagonal:
                max_area = max(max_area, l * w)
        return max_area

