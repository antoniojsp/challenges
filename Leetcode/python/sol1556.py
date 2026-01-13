# https://leetcode.com/problems/thousand-separator/description/
class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = str(n)
        result = []
        counter = 0
        for i in num[::-1]:
            if counter < 3:
                result.append(i)
            else:
                result.append(f"{i}.")
                counter = 0
            counter += 1
        return "".join(result[::-1])


