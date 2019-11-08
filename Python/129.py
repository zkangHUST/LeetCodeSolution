# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, root, num):
        if not root:
            return 
        num = num * 10 + root.val
        if not root.left and not root.right:
            self.ans += num
            return 
        self.dfs(root.left, num)
        self.dfs(root.right, num)
        