#  https://leetcode.com/problems/clear-digits/
class Solution:
    def clearDigits(self, s: str) -> str:

        stack = []
        for i, j in enumerate(s, start=1):
            if j.isalpha():
                stack.append(j)
            else:
                stack.pop()

        return "".join(stack)

