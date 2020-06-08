# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        key = self.find(root, x)
        if not key:
            return False 
        a, b = self.count(key.left), self.count(key.right)
        c = n - a - b - 1
        m = max(a, b, c)
        if (m << 1) > n:
            return True
        return False
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
    def find(self, root, x):
        if not root:
            return None
        if root.val == x:
            return root
        a = self.find(root.left, x)
        return a if a else self.find(root.right, x)