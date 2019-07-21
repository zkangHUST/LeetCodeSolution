# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s = []
        self.inOrdertravel(root, s, k)
        return s[k - 1]

    def inOrdertravel(self, root, s, k):
        if len(s) >= k:
            return
        if not root:
            return
        self.inOrdertravel(root.left, s, k)
        s.append(root.val)
        self.inOrdertravel(root.right, s, k)