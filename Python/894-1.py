# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        if N % 2 == 0:
            return []
        if (N == 1) :
            return [0]
        i = 1
        j = N - 1 -i
        



                