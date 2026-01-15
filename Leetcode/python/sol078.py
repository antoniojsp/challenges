
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=problem-list-v2&envId=greedy


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        color_start = colors[0]
        color_end = colors[-1]
        left = [len(colors) - 1 - i for i in range(0, len(colors)) if colors[i] != color_end][0]
        right = [i for i in range(len(colors) - 1, 0, -1) if colors[i] != color_start][0]

        return max(left, right)
