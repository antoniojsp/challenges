
# https://leetcode.com/problems/alternating-groups-i/description/

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        length = len(colors)
        for curr in range(length):
            prev = curr - 1
            following = (curr+1)%length
            if (colors[prev] == colors[following]) and colors[curr] != colors[prev ]:
                count += 1
        return count