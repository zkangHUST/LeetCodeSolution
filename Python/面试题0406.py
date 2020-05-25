# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.ans = []
        self.inorderTravel(root, p)
        if len(self.ans) < 2:
            return None
        # print(self.ans)
        return self.ans[1]
    def inorderTravel(self, root, p):
        # print(self.ans)
        if not root:
            return 
        self.inorderTravel(root.left, p)
        if len(self.ans) == 2:
            return 
        if root == p:
            self.ans.append(root)
        elif len(self.ans) == 1:
            self.ans.append(root)
        if len(self.ans) == 2:
            return
        self.inorderTravel(root.right, p)
            
