# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/submissions/1623561067/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    @staticmethod
    def average(root :TreeNode) -> int:
        Q = [root]
        suma = 0
        count = 0
        while Q:
            temp = Q.pop(0)
            suma += temp.val
            count +=1
            if temp.left:
                Q.append(temp.left)
            if temp.right:
                Q.append(temp.right)

        average = int(suma /count)
        return average

    def averageOfSubtree(self, root: TreeNode) -> int:

        Q = [root]
        count = 0
        while Q:
            temp = Q.pop(0)
            if temp.val == self.average(temp):
                count+=1

            if temp.left:
                Q.append(temp.left)
            if temp.right:
                Q.append(temp.right)

        return count
