class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        exp = 0
        while 0 < n:
            val = (n % 10) * 10 ** exp
            if val != 0:
                result.append(val)
            n //= 10
            exp += 1
        return result[::-1]





