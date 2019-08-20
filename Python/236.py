# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        self.pathx = []
        self.pathy = []
        path = []
        self.dfs(root, p, q, path)
        minlen = min(len(self.pathx), len(self.pathy))
        for i in range(minlen):
            if self.pathx[i] != self.pathy[i]:
                return self.pathx[i - 1]
        return self.pathx[minlen - 1]
        
    def dfs(self, root, x, y, path):
        if not root:
            return 
        path.append(root)
        if root.val == x.val:
            self.pathx = path
        if root.val == y.val:
            self.pathy = path
        if self.pathx and self.pathy:
            return 
        self.dfs(root.left, x, y, path[:])
        self.dfs(root.right, x, y, path[:])