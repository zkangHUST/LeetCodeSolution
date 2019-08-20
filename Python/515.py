# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        cnt = 1
        nextcnt = 0
        tmp = root.val
        while stack:
            if cnt > 0:
                cnt -= 1
                n = stack.pop(0)
                tmp = max(tmp, n.val)
                if n.left:
                    stack.append(n.left)
                    nextcnt += 1
                if n.right:
                    stack.append(n.right)
                    nextcnt += 1
            else:
                cnt = nextcnt 
                nextcnt = 0
                res.append(tmp)
                tmp = -math.inf
        res.append(tmp)
        return res