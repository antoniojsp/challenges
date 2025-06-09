# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
from collections import defaultdict

class Solution:

    def create_adj_list(self, n, edges :List[List[int]]):
        adj_list = defaultdict(list)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        return adj_list

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj_list = self.create_adj_list(n, edges)
        S = [source]
        seen = set()
        seen.add(source)
        while S:
            curr_node = S.pop()
            if curr_node == destination:
                return True

            for node in adj_list[curr_node]:
                if node not in seen:
                    S.append(node)
                    seen.add(node)

        return False


# recursive

from collections import deque, defaultdict


class Solution:
    def create_adj_list(self, edges: List[List[int]]) -> defaultdict[int, List[int]]:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = self.create_adj_list(edges)
        seen = set()

        def dfs(current):
            if current == destination:
                return True
            seen.add(current)
            for i in adj_list[current]:
                if i not in seen:
                    if dfs(i):
                        return True
            return False

        return dfs(source)





