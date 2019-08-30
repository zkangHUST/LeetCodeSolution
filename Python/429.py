"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans 
        stack = []
        stack.append(root)
        cnt = 1
        nextcnt = 0
        ans.append([root.val])
        vlist = []
        while len(stack) > 0:
            if cnt > 0:
                tmp = stack.pop(0)
                cnt -= 1
                for item in tmp.children:
                    vlist.append(item.val)
                    stack.append(item)
                    nextcnt += 1
            else:
                ans.append(vlist[:])
                vlist.clear()
                cnt = nextcnt 
                nextcnt = 0
        return ans
        