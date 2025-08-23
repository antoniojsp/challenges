
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = " ".join([s 1 +"  " +s2]).split()
        count_words = Counter(words)

        return [word for word in count_words if count_words[word] == 1]
