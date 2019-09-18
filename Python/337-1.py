# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.get(root))
    def get(self, root: TreeNode) -> int:
        if not root:
            return [0,0]
        l = self.get(root.left)
        r = self.get(root.right)
        return [max(l) + max(r), l[0] + r[0] + root.val]
