
#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operand = {
            "--X": lambda x: x-1,
            "X--": lambda x: x-1,
            "++X": lambda x: x+1,
            "X++": lambda x: x+1,
        }
        initial_value = 0
        for i in operations:
            initial_value = operand[i](initial_value)
        return initial_value