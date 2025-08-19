
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)-2):
            substring = set(s[i:i+3])
            if len(substring) == 3:
                count+=1

        return count

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        freq = Counter(s[0:3])
        count = 1 if len(freq) == 3 else 0
        for i in range(0, len(s) - 3):
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                del freq[s[i]]
            freq[s[i + 3]] = freq.get(s[i + 3], 0) + 1
            if len(freq) == 3:
                count += 1

        return count





