# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = []
        self.dfs(root, 0)
        return sum(self.res)
    def dfs(self, root, val):
        if not root:
            return
        val = val * 2 + root.val
        if not root.left and not root.right:
            self.res.append(val)
        self.dfs(root.left, val)
        self.dfs(root.right, val)
