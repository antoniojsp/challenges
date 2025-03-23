class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        seen = set()
        count = 0
        for i in words:
            temp = "".join(sorted(i))
            if temp in seen:
                count += 1
            else:
                seen.add(temp)
        return count
