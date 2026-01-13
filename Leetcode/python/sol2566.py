# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def max_possible_value(self, num :int) -> int:
        val = str(num)
        digit = ""
        for i in val:
            if i != "9":
                return int(val.replace(i, "9"))
        return num

    def min_possible_value(self, num :int) -> int:
        val = str(num)
        most_left_digit = val[0]
        return int(val.replace(most_left_digit, "0"))

    def minMaxDifference(self, num: int) -> int:
        return self.max_possible_value(num) - self.min_possible_value(num)

