# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/1748359574/

class Solution:
    def build_freq_arr(self, string:str)->List[int]:
        '''
        Creates a frequency array
        '''
        freq_arr = [0]*26
        for i in string:
            freq_arr[ord(i)-ord('a')]+=1
        return freq_arr

    def minSteps(self, s: str, t: str) -> int:
        '''
        Creates 2 freq lists with s and t, compare each index in both lists and sum up the difference
        return the sum difference divided by 2.
        By constraint, both strings have the same length, hence, no checking if there is a mismatch in size.
        '''
        count = 0
        arr_s = self.build_freq_arr(s)
        arr_t = self.build_freq_arr(t)
        for i, j in zip(arr_s, arr_t):
            count += abs(i-j)
        return count//2