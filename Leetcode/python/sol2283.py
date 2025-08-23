# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
class Solution:
    def digitCount(self, num: str) -> bool:
        freq = Counter(num)
        for i in range(len(num)):
            if freq[str(i)] != int(num[i]):
                return False
        return True


class Solution:
    def digitCount(self, num: str) -> bool:
        freq = {}
        for i in num:  # Counter
            freq[int(i)] = freq.get(int(i), 0) + 1

        for i in range(len(num)):
            if freq.get(i, 0) != int(num[i]):  # if i not present in str, then freq is 0 (use get to avoid key errors)
                return False
        return True
