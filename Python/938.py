# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):    
        self.sum = 0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if (root.val > R):
           self.rangeSumBST(root.left, L, R)
        elif (root.val < L):
            return  self.rangeSumBST(root.right, L, R)
        else:
            self.sum += root.val
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)
        return self.sum


    
