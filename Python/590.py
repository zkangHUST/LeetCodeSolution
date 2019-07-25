"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.ans = []
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return 
        for ch in root.children:
            self.postorder(ch)
        self.ans.append(root.val)
        return self.ans