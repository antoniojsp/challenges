# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root: return res
        res.append(root.val)

        def dfs(node):
            if not node:
                return None
            for c in node.children:
                res.append(c.val)
                dfs(c)
        dfs(root)
        return res