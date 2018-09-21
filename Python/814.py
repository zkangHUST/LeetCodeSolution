# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """     
        fakeHead = TreeNode(1)
        fakeHead.right = root
        self.travel(fakeHead)
        return root
    def travel(self, root):
        if (root == None):
            return True
        if (self.travel(root.left) == True):
            root.left = None    
        if (self.travel(root.right) == True):
            root.right = None    
        if (root.left == None and root.right == None  and root.val == 0):
            return True  