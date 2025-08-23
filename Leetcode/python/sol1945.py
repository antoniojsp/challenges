# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/1745246634/
class Solution:
    def letter_map(self, s :str)->str:
        string_nums = "".join(str(ord(i) - ord('a' ) +1) for i in s)
        return string_nums

    def getLucky(self, s: str, k: int) -> int:
        str_value = self.letter_map(s) # initial convert string chars to numbers
        for _ in range(k):
            str_value = str(sum(map(int, str_value))) # sums te result nd convert it again to string for the next loop
        return int(str_value)


