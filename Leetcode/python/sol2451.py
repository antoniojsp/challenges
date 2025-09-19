#  https://leetcode.com/problems/odd-string-difference/
class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = []
        for word in words:
            temp = []
            for i in range(1, len(word)):
                temp.append(ord(word[i] ) -ord(word[ i -1]))
            diff.append((word, tuple(temp)))

        counter = defaultdict(int)
        for i, j in diff:
            counter[j]+=1
        # print(counter)
        temp = None
        for i, j in counter.items():
            if j == 1:
                temp = i
                break

        for i in diff:
            if i[1] == temp:
                return i[0]






