
# https://leetcode.com/problems/all-paths-from-source-to-target/description/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end_goal = len(graph) - 1
        S = [(0,[0])]
        ans = []
        while S:
            node, path = S.pop()
            if node == end_goal:
                ans.append(path)
            for j in graph[node]:
                S.append((j, path+[j]))
        return ans