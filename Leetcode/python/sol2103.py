

# https://leetcode.com/problems/rings-and-rods/description/
class Solution:
    def countPoints(self, rings: str) -> int:

        rods = {}
        for i in range(0, len(rings), 2):
            rods[rings[i: i +2][1]] = rods.get(rings[i: i +2][1], set())
            rods[rings[i: i +2][1]].add(rings[i: i +2][0])
        return sum([1 for i in rods.values() if len(i) == 3])


class Solution:
    def countPoints(self, rings: str) -> int:
        rods: dict[str, set[str]] = defaultdict(set)
        for i in range(0, len(rings), 2):
            rods[rings[i + 1]].add(rings[i])

        return sum(1 for i in rods.values() if len(i) == 3)