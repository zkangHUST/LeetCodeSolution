# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = self.getheight(root)
        #树的宽度 w = 2^h - 1        
        w = (1 << h) - 1 
        ans = [["" for i in range(w)] for j in range(h)]
        self.fillData(root, ans, 0, w - 1, 0)
        return ans
    # 返回树的高度     
    def getheight(self, root):
        if not root:
            return 0
        return 1 + max(self.getheight(root.left), self.getheight(root.right))

    def fillData(self, root, ans, l, r, i):
        if not root:
            return 
        mid = l + (r - l) // 2
        ans[i][mid] = str(root.val)
        self.fillData(root.left, ans, l, mid - 1, i + 1)
        self.fillData(root.right, ans, mid + 1, r, i + 1)
        
        