# https://leetcode.com/problems/baseball-game/description/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            match i:
                case "+":
                    temp = stack[-1 ] +stack[-2]
                    stack.append(temp)
                case "C":
                    stack.pop()
                case "D":
                    stack.append(stack[-1 ] *2)
                case _:
                    stack.append(int(i))
        return sum(stack)
