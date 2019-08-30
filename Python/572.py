# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.sametree(s, t):
            return True
        if s.left and self.isSubtree(s.left, t):
            return True
        if s.right and self.isSubtree(s.right, t):
            return True
        return False
    def sametree(self, t1, t2):
        if not t1 and  not t2:
            return True
        if not t1 :
            return False
        if not t2:
            return False
        if t1.val != t2.val:
            return False
        if t1.val == t2.val:
            l = self.sametree(t1.left, t2.left)
            r = self.sametree(t1.right, t2.right)
            return (l and r)
        