# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a,b = [], []
        self.getElements(root1, a)
        self.getElements(root2, b)
        ans = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1
        if i < len(a):
            ans += a[i:]
        if j < len(b):
            ans += b[j:]
        return ans
    def getElements(self, root, ans):
        if not root:
            return 
        if root.left:
            self.getElements(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.getElements(root.right, ans)
    