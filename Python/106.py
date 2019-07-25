# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        r = TreeNode(0)
        r.val = postorder[-1]
        i = inorder.index(r.val)
        lpos = postorder[0:i]
        rpos = postorder[i: -1]
        lino = inorder[0:i]
        rino = inorder[i+1:]
        r.left = self.buildTree(lino, lpos)
        r.right = self.buildTree(rino, rpos)
        return r