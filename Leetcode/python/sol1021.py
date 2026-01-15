# https://leetcode.com/problems/remove-outermost-parentheses/


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        degree = 0
        for i in s:
            if i == "(":
                if 0 < degree:
                    result.append(i)
                degree += 1
            elif i == ")":
                degree -= 1
                if 0 < degree:
                    result.append(i)
        return "".join(result)

