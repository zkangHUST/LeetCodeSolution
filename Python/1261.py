# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.cnt = {0}
        self.recover(root)

    def find(self, target: int) -> bool:
        if target in self.cnt:
            return True
        return False
    def recover(self, root):
        if root.left:
            root.left.val = root.val * 2 + 1
            self.cnt.add(root.left.val)
            self.recover(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self.cnt.add(root.right.val)
            self.recover(root.right)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)