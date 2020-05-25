# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.cnt = 0
        self.dfs(root, [], sum)
        return self.cnt

    def dfs(self, root, path, sum):
        if not root:
            return 
        if root.val == sum:
            self.cnt += 1
        for i in range(len(path)):
            path[i] += root.val
            if path[i] == sum:
                self.cnt += 1
        path.append(root.val)
        self.dfs(root.left, path[:], sum)
        self.dfs(root.right, path[:], sum)