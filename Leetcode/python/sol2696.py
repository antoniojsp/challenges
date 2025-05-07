
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if stack:
                if i == "B" and stack[-1] == "A":
                    stack.pop()
                elif i == "D" and stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return len(stack)
        # while True:
        #     length = len(s)
        #     s = s.replace("AB", "").replace("CD", "")
        #     if length == len(s):
        #         return len(s)




