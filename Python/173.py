# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.s = []
        self.travel(root, self.s)
        self.i = 0
        self.length = len(self.s)
        

    def next(self) -> int:
        
        if self.i < self.length:
            tmp = self.i
            self.i += 1
            return self.s[tmp]
        """
        @return the next smallest number
        """
        

    def hasNext(self) -> bool:
        if self.i < self.length:
            return True
        return False
        """
        @return whether we have a next smallest number
        """
    def travel(self, root, s):
        if not root:
            return 
        self.travel(root.left, s)
        s.append(root.val)
        self.travel(root.right, s)
        
            


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()