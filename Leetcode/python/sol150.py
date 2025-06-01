
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        set_operators = set("+-*/")
        for i in tokens:
            if i in set_operators:
                val_a = stack.pop()
                val_b = stack.pop()
                temp = 0
                match i:
                    case "+":
                        temp = val_a + val_b
                    case "-":
                        temp = val_b - val_a
                    case "/":
                        temp = int(val_b / val_a)
                    case "*":
                        temp = val_b * val_a
                stack.append(temp)
            else:
                stack.append(int(i))

        return stack[0]