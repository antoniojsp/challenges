# https://leetcode.com/problems/majority-frequency-characters/
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s) # count freq chars

        freq_of_freqs = defaultdict(list)
        for char, num in freq.items(): #
            freq_of_freqs[num].append(char)

        max_freq = max(len(lista) for i, lista in freq_of_freqs.items())
        results = {key: lista for key, lista in freq_of_freqs.items() if max_freq == len(lista)}
        max_key = max(results.keys())
        return "".join(results[max_key])


