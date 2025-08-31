# https://leetcode.com/problems/find-the-least-frequent-digit/
class Solution:
    def separate_digits(self, n :int) -> List[int]:
        digits = []
        while 0 < n:
            digits.append( n %10)
            n//=10
        return digits

    def search_min_freq(self, digits:list) -> int :
        freq_arr = [0]*10

        for i in digits:
            freq_arr[i]+=1

        minimum = float('inf')
        index = 0
        for idx, freq in enumerate(freq_arr):
            if freq != 0 and freq < minimum:
                minimum = freq
                index = idx

        return index

    def getLeastFrequentDigit(self, n: int) -> int:
        digits = self.separate_digits(n) # we could use str()   o convert the int, but using custom function.
        return self.search_min_freq(digits)