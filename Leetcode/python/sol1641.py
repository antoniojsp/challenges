# https://leetcode.com/problems/count-sorted-vowel-strings/description/
class Solution:
    def countVowelStrings(self, n: int) -> int:
        table = [[0 ] *5 for i in range( n +1)]
        for i in range(5): # fill first row of 1, meaning that with one char it can be only formed a string of 1 char
            table[1][i]  = 1
        for i in range(2, n+ 1):
            temp = sum(table[i - 1])
            table[i][0] = temp
            for j in range(1, 5):
                table[i][j] = table[i][j - 1] - table[i - 1][j - 1]
        return sum(table[n])


class Solution:
    def countVowelStrings(self, n: int) -> int:
        num_vowels = 5
        dp = [1]*num_vowels
        for i in range(2, n+1):
            for j in range(num_vowels-2, -1, -1):
                dp[j] = dp[j+1]+dp[j]
        return sum(dp)