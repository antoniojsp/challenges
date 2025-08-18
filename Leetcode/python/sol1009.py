
# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
      binary =  bin(n)[2:]
      rslt = 0
      exp = 0
      for i in range(len(binary)-1, -1, -1):
        if binary[i] == "0":
          rslt+=2**exp
        exp+=1
      return rslt

