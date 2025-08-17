
# https://leetcode.com/problems/number-of-even-and-odd-bits/
class Solution:

    def bin_form(self, n:int) -> list:
        binary = []
        while 0 < n:
            binary.append(n%2)
            n //= 2
        return binary

    def evenOddBit(self, n: int) -> List[int]:
        binary = self.bin_form(n)
        even = 0
        odd = 0
        for i, v in enumerate(binary):
            if v == 1:
                if i % 2 == 0:
                    even+=1
                else:
                    odd+=1

        return [even, odd]