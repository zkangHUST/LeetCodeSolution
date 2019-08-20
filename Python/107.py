# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return 
        stack = []
        stack.append(root)
        cnt = 1
        nextcnt = 0
        s = []
        res = []
        while len(stack)  > 0:
            if cnt > 0:
                cnt -= 1
                tmp = stack.pop(0)
                s.append(tmp.val)
                if tmp.left :
                    stack.append(tmp.left)
                    nextcnt += 1
                if tmp.right:
                    stack.append(tmp.right)
                    nextcnt += 1
            else:
                cnt = nextcnt
                nextcnt = 0
                res.append(s[:])
                s.clear()
        res.append(s[:])
        return res[::-1]
        