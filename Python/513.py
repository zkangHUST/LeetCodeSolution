# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        if not root.left and not root.right:
            return root.val
        if self.height(root.left) >= self.height(root.right):
            return self.findBottomLeftValue(root.left)
        return self.findBottomLeftValue(root.right)
        

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
