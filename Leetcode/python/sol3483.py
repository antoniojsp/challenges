# https://leetcode.com/problems/unique-3-digit-even-numbers/description/

class Solution:
    def compare(self, available, needs):
        for i in needs:
            if available[i] < needs[i]:
                return False
        return True

    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        counter = Counter(digits)

        for i in range(1,10):
            for j in range(0,10):
                for k in range(0, 10, 2):
                    if self.compare(counter, Counter([i,j,k])):
                        count+=1
        return count
