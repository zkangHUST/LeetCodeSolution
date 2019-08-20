# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1): 
            return False
        if root1.val != root2.val:
            return False
        a = self.flipEquiv(root1.left, root2.left)  
        b = self.flipEquiv(root1.right, root2.right)
        c = self.flipEquiv(root1.left, root2.right)
        d = self.flipEquiv(root1.right, root2.left)

        if ( a and b ) or (c and d):
            return True
        return False  

