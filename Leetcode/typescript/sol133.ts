
//https://leetcode.com/problems/clone-graph/description/

/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     neighbors: _Node[]
 *
 *     constructor(val?: number, neighbors?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 *
 */


function cloneGraph(node: _Node | null): _Node | null {
    if(!node){
        return node;
    }
	const Q:_Node[] = [node];
    const mapa:Map<_Node, _Node> = new Map();
    // mapa < node original, node copy >
    mapa.set(node, new _Node(node.val));
    while(Q.length > 0){
        const curr:_Node | undefined = Q.shift();
        for(const i of curr.neighbors){
            if(!mapa.has(i)){
                mapa.set(i, new _Node(i.val));
                Q.push(i);
            }
            mapa.get(curr).neighbors.push(mapa.get(i))
        }
    }
    return mapa.get(node);
};




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


