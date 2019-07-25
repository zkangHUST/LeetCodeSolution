# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        r = TreeNode(0)
        r.val = preorder[0]
        i = inorder.index(r.val)
        lpre = preorder[1:i+1]
        rpre = preorder[i + 1:]
        lino = inorder[0:i]
        rino = inorder[i+1:]
        r.left = self.buildTree(lpre, lino)
        r.right = self.buildTree(rpre, rino)
        return r