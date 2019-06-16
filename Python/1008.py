# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        for val in preorder:
            root = self.insert(root, val)
        return root
    def insert(self, root, value):
        if not root:
            root = TreeNode(value)
            return root
        tmp = TreeNode(value)
        node = root
        while(node):
            if (value < node.val):
                if not node.left:
                    node.left = tmp
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = tmp
                    break
                else:
                    node = node.right
        return root
        

