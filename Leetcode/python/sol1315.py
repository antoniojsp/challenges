# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        Q = deque() # root, parent, grandparent
        Q.append((root, None, None)) # keep track of parent and grandparent
        result = 0 # sum of nodes with even value grandparents
        while Q:
            node, parent, grandparent = Q.popleft()
            if node:
                if grandparent and grandparent.val%2 == 0:
                    result+=node.val
                if node.left: # adding childs
                    Q.append((node.left, node, parent)) #  add left child, the current node is the father, and the current node father becomes the grandfather.
                if node.right:
                    Q.append((node.right, node, parent))
        return result