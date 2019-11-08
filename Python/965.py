# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.travel(root, root.val)

    def travel(self, root, val):
        if not root:
            return True
        if root.val != val:
            return False
        if not self.travel(root.left, val):
            return False
        if not self.travel(root.right, val):
            return False
        return True
    