# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x = 0
        self.y = 0
        self.dfs(root, x, y)
        return self.x == self.y 
    def dfs(self, root, x, y, path):
        if not root:
            return 
        path.append(root.val)
        if root == x:
            self.x = len(path)
            return 
        if root == y:
            self.y = len(path)
            return 
        self.dfs(root.left, path[:])
        self.dfs(root.right,path[:])
