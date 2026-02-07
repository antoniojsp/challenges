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
        node_copy = Node(val=node.val, neighbors = [])
        print(node_copy.val)

        Q = deque([node, node_copy])
        seen = set()
        while Q:
            node, cnode = Q.popleft()
            print(node.val)
            if node and node not in seen:
                seen.add(node)
                for i in node.neighbors:
                    temp = Node(val=i.val ,neighbors = [])
                    Q.append([i, temp])

        return


