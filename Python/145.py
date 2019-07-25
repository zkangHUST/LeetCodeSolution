# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        self.ans.append(root.val)
        self.postorderTraversal(root.right)
        self.postorderTraversal(root.left)
        tmp = self.ans[::-1]
        return tmp