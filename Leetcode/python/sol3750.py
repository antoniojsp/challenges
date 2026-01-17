# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/submissions/1887716292/
class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = f"{n:b}"
        count = 0
        for idx in range(len(binary)//2):
            if binary[idx] != binary[~idx]:
                count+=1
        return count*2


