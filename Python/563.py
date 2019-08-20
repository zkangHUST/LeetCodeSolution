# 虽然通过了，但是速度巨慢
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    def dfs(self, root):
        if not root:
            return 
        self.ans += self.gettilt(root)
        if not root.left and not root.right:
            return 
        self.dfs(root.left)
        self.dfs(root.right)
        
    def gettilt(self, root):
        if not root:
            return 0
        l = self.getsum(root.left)
        r = self.getsum(root.right)
        return abs(l - r)
    def getsum(self, root):
        if not root:
            return 0
        return root.val + self.getsum(root.left) + self.getsum(root.right)