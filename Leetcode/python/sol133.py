# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        Q = deque([node])
        seen = set()
        clone_map = defaultdict(list)
        # result = Node(val=)

        while Q:
            node = Q.popleft()
            if node in seen:
                continue
            if node:
                # print(node.val)
                seen.add(node)
                for i in node.neighbors:
                    clone_map[node.val].append(i.val)
                    Q.append(i)


        print(clone_map)


