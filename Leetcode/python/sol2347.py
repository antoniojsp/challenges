# https://leetcode.com/problems/best-poker-hand/
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank = Counter(ranks)
        suit = Counter(suits)

        if any(i == 5 for i in suit.values()):
            return "Flush"
        elif any(i >= 3  for i in rank.values()):
            return "Three of a Kind"
        elif any(i == 2 for i in rank.values()):
            return "Pair"
        return "High Card"
