
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/solutions/7244060/separation-of-concerns-by-antoniojsp-4yw5/

class Solution:
    def to_hex(self, num: int):
        """
        Convert decimals to hexadecimal
        """
        letters = "0123456789abcdef"
        result = ""
        while 0 < num:
            result += letters[num % 16]
            num //= 16
        return result[::-1]

    def two_complement_negative(self, val):
        """
        For negatie numbers
        """
        bits = [0] * 32
        binary = format(-val - 1, "032b")
        result = 0
        exp = 0
        for i in range(len(binary) - 1, -1, -1):
            if binary[i] == "0":
                result += 2 ** exp
            exp += 1
        return result

    def toHex(self, num: int) -> str:
        result = "0"
        if num > 0:
            result = self.to_hex(num)
        elif num < 0:
            temp = self.two_complement_negative(num)
            result = self.to_hex(temp)
        return result



