# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        self.move(root)
        return self.ans 
    def move(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            num = root.val - 1
            if num != 0:
                self.ans += abs(num)
            return num
        a = self.move(root.left)
        b = self.move(root.right)
        root.val += (a + b)
        if root.val - 1 != 0:
            self.ans += abs(root.val - 1)
        return root.val - 1


