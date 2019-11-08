# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        r = TreeNode(0)
        if not t2:
            r = t1
            return r
        if not t1:
            r = t2
            return r
        r.val = t1.val + t2.val
        r.left = self.mergeTrees(t1.left, t2.left)
        r.right = self.mergeTrees(t1.right, t2.right)
        return r