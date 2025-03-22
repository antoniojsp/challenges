class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        count = s.count("1")
        length = len(s)

        left = count - 1
        zeros = length - count
        result = "1" # since there is at least one "1"

        for i in range(zeros):
            result = "0" + result

        for i in range(left):
            result = "1" + result

        return result