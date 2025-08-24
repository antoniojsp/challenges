
# https://leetcode.com/problems/count-common-words-with-one-occurrence/solutions/7114894/using-counter-and-intersection-by-antoni-8qgx/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        intersection = c1 & c2
        count = 0
        for i in intersection:
            if c1[i] == 1 and c2[i] == 1:
                count+=1
        return count

        # using sets and counters
        # set1 = set(words1)
        # set2 = set(words2)
        # intersect = set1.intersection(set2)
        # count = 0
        # counter1 = Counter(words1)
        # counter2 = Counter(words2)
        # for i in intersect:
        #     if counter1[i] == 1 and counter2[i] == 1:
        #         count+=1
        # return count