# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.res = []
        path = []
        self.dfs(root, path)
        if len(self.res) == 1:
            return self.res[0][-1]
        for i in range(len(self.res[0])):
            for j in range(len(self.res) - 1):
                if self.res[j][i] != self.res[j + 1][i]:
                    return self.res[j][i - 1]
        
    def dfs(self, root, path):
        if not root:
            return 
        path.append(root)
        if not root.left and not root.right:
            if not self.res :
                self.res.append(path)
            else:
                if len(path) >  len(self.res[0]):
                    self.res.clear()
                    self.res.append(path)  
                elif len(path) == len(self.res[0]):
                    self.res.append(path)
            return 
        self.dfs(root.left, path[:])
        self.dfs(root.right, path[:])
        
                    
        