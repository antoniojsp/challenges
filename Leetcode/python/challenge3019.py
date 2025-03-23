class Solution:
    def countKeyChanges(self, s: str) -> int:
        temp = s.lower()
        count = 0
        for i in range(len(temp)-1):
            if temp[i] != temp[i+1]:
                count+=1

        return count