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

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from pprint import pprint
from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        mapa = {}
        mapa[node] = Node(val=node.val)

        def helper(n):
            for i in n.neighbors:
                if i not in mapa:
                    mapa[i] = Node(val=i.val)
                    helper(i)
                mapa[n].neighbors.append(mapa[i])

        helper(node)
        return mapa[node]
        # if not node:
        #     return None
        # Q = deque([node])
        # mapa = {}
        # mapa[node] = Node(val=node.val)
        # while Q:
        #     curr = Q.popleft()
        #     for i in curr.neighbors:
        #         if i not in mapa:
        #             mapa[i] = Node(val=i.val)
        #             Q.append(i)
        #         mapa[curr].neighbors.append(mapa[i])
        # return mapa[node]








