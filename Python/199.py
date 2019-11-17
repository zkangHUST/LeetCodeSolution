# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return 
        stack = [root]
        cnt = 1
        nextcnt = 0
        while stack:
            if cnt > 0:
                cnt -= 1
                node = stack.pop(0)
                if cnt == 0:
                    ans.append(node.val)
                if node.left:
                    stack.append(node.left)
                    nextcnt += 1
                if node.right:
                    stack.append(node.right)
                    nextcnt += 1
            else:
                cnt = nextcnt
                nextcnt = 0
        return ans