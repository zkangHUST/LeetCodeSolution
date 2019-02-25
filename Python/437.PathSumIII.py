# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    cnt = 0
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        res = []
        self.travel(root, res, sum)
        return self.cnt
    def travel(self, root, res, sum):
        if (root == None):
            return 
        for i in range(len(res)):
            res[i] += root.val
            if res[i] == sum:
                self.cnt += 1
        res.append(root.val)
        if (root.val == sum):
            self.cnt += 1
        if root.left:
            self.travel(root.left, res[:], sum)
        if root.right:
            self.travel(root.right, res[:], sum)
