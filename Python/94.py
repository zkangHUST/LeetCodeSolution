# Definition for a binary tree node.
class TreeNode:
  
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.travel(root,l)
        return l
    def travel(self, root, l):
        if(root == None):
            return 
        self.travel(root.left, l)
        l.append(root.val)
        self.travel(root.right, l)

        