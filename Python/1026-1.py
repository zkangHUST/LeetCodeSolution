# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.maxdiff = 0
        self.dfs(root, root.val, root.val)
        return self.maxdiff
    def dfs(self, root, minval, maxval):
        if not root:
            return 
        minval = min(root.val, minval)
        maxval = max(root.val, maxval)
        if not root.left and not root.right:
            if (maxval - minval) > self.maxdiff:
                self.maxdiff = (maxval - minval) 
            return
        self.dfs(root.left, minval, maxval)
        self.dfs(root.right, minval, maxval)