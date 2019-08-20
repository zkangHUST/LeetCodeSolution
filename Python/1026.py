# 这个方法超时了，有一个case过不了
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.maxAncestorDiff(root.left)
        r = self.maxAncestorDiff(root.right)
        tmp = self.maxdiff(root, 0, root.val)
        return max(l, r, tmp)
    def maxdiff(self, root, res, initvalue):
        if not root:
            return res
        l = self.maxdiff(root.left, res, initvalue)
        r = self.maxdiff(root.right, res, initvalue)
        res = max(l, r)
        if abs(root.val - initvalue) > res:
            res = abs(root.val - initvalue)
        return res


        