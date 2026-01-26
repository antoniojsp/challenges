# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        reverse = False
        while 0 < time:
            if not reverse:
                i+=1
            else:
                i-=1
            time-=1
            if i == 1 or i == n:
                reverse = not reverse
        return i