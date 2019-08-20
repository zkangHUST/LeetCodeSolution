"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        stack.append(root)
        cnt = 1
        nextcnt = 0
        prev = fakehead = Node()
        while len(stack) > 0:
            while cnt > 0:
                cnt -= 1
                tmp = stack.pop(0)
                prev.next = tmp
                prev = tmp
                if cnt == 0:
                    tmp.next = None
                if tmp.left:
                    stack.append(tmp.left)
                    nextcnt += 1
                if tmp.right:
                    stack.append(tmp.right)
                    nextcnt += 1
            prev = fakehead
            cnt = nextcnt
            nextcnt = 0
        return root



