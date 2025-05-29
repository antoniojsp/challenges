# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        brackets = {']':'[', '}':'{', ')':'('}
        for i in s:
            if i in brackets:
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0

