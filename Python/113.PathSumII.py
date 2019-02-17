# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    s = []
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        s = []
        res = []
        self.travel(root, res, sum, s)
        return s
    def travel(self, root, res, ans, s):
        if (root == None):
            return
        if (root.left == None and root.right == None):
            res.append(root.val)
            if sum(res) == ans:
                s.append(res)
        else:
            res.append(root.val)
            if root.left:
                self.travel(root.left, res[:], ans, s)
            if root.right:
                self.travel(root.right, res[:], ans, s)