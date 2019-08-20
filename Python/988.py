# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.res = ""
        path = ""
        self.dfs(root, path)
        return self.res
    def dfs(self, root, path):
        if not root:
            return 
        path += chr(root.val + 97)  
        if not root.left and not root.right:
            if not self.res:
                self.res = path[::-1]
            elif path[::-1] < self.res:
                self.res = path[::-1]
            return 
        self.dfs(root.left, path[:])
        self.dfs(root.right, path[:])
        
            
        