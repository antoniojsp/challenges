class Solution:
    def countAsterisks(self, s: str) -> int:

        signal = False
        count = 0
        for i in s:
            if signal == False and i == "*":
                count += 1

            if i == "|":
                signal = not signal

        return count