#  https://leetcode.com/problems/crawler-log-folder/description/


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack:list[int] = []
        for i in logs:
            if i == "../":
                if stack:
                    stack.pop()
            elif i != "./":
                stack.append(i)
        return len(stack)