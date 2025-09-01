# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/?envType=problem-list-v2&envId=string
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split() # splits tokens
        values = [int(i) for i in s if i.isdigit()] # filter the number string in the setence and convert to int
        for i in range(len(values ) -1):
            if values[i] >= values[ i +1]: # check if it's strictly increasing
                return False
        return True

