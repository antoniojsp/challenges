# https://leetcode.com/problems/merge-similar-items/description/
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        merge :list[int] = items1 + items2
        elements :dict[int ,int] = {}
        for i, j in merge:
            elements[i] = elements.get(i, 0) + j
        rslt :list[int] = list(elements.items())
        rslt.sort(key=lambda x: x[0], reverse=False)
        return rslt
