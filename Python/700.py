# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        p = root
        while (p != None):
            if (p.val < val):
                p = p.right
            elif (p.val > val):
                p = p.left
            else:
                return p
        return None
