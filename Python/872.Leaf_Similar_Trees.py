# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        s1 = []
        s2 = []
        self.travel(root1, s1)
        self.travel(root2, s2)
        if (s1 == s2):
            return True
        else:
            return False
    def travel(self, root, quence):
        if (root == None):
            return 
        elif(root.left == None and root.right == None):
            quence.append(root.val)
        else:
            if (root.left):
                self.travel(root.left, quence)
            if (root.right):
                self.travel(root.right, quence)
