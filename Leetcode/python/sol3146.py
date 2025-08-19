
# https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def key_index(self, string:str):
        '''
        Since the constraints claim that the characters are unique, then using a dictionary works fine.
        '''
        return {char:idx for idx, char in enumerate(string)}

    def findPermutationDifference(self, s: str, t: str) -> int:
        s_index = self.key_index(s)
        t_index = self.key_index(t)

        return sum(abs(s_index[i]-t_index[i]) for i in s)