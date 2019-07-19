# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        fakehead = TreeNode(-1)
        tail = fakehead
        self.travel(root, tail)
        return fakehead.right
    def travel(self, root, tail):
        if root == None:
            return tail
        tail = self.travel(root.left, tail)
        tmp = TreeNode(root.val)
        tail.right = tmp
        tail = tmp
        tail = self.travel(root.right, tail)
        return tail