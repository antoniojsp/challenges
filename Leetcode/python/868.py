# https://leetcode.com/problems/binary-gap/
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        last_seen = None
        max_dist = 0
        for i in range(len(binary)):
            if last_seen is None and binary[i] == '1':
                last_seen = i
            elif binary[i] == '1':
                max_dist = max(max_dist, i - last_seen)
                last_seen = i
        return max_dist
