# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.mindiff = math.inf
        buf = []
        self.dfs(root, buf)
        return self.mindiff
    def dfs(self, root, buf):
        if not root:
            return 
        self.dfs(root.left, buf)
        if not buf:
            buf.append(root.val)
        else:
            diff = abs(root.val - buf[0])
            buf.clear()
            buf.append(root.val)
            if diff < self.mindiff:
                self.mindiff = diff 
        self.dfs(root.right, buf)
        