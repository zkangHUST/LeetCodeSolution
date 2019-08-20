# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.maxlength(root)
    def maxlength(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        l = self.maxlength(root.left)
        r = self.maxlength(root.right)
        p = self.levels(root.left) + self.levels(root.right)
        return max(l, r, p)
    def levels(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 +  max(self.levels(root.left), self.levels(root.right))
    
        