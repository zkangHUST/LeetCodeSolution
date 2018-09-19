# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = TreeNode(val)
        p = root
        while (p != None):
            if (p.val < val):
                if (p.right == None):
                    p.right = node
                    break 
                p = p.right
            else:
                if (p.left == None):
                    p.left = node
                    break 
                p = p.left
        return root
            