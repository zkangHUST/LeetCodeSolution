# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = []
        return self.travel(root,l)
    def travel(self, root, l):
        if(root == None):
            return True
        if(self.travel(root.left,l) == False):
            return False
        if l and root.val < l[-1]:
            return False
        l.append(root.val)
        if(self.travel(root.right,l) == False):
            return False
        return True