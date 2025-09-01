# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/
class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        max_chairs = 0
        for i in s:
            match i:
                case "E":
                    count+=1
                case "L":
                    count-=1
            max_chairs = max(max_chairs, count)
        return max_chairs
