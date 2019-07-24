class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p1 = []
        p2 = []
        self.travel(root, p, p1)
        self.travel(root, q, p2)
        i = len(p1) - 1
        j = len(p2) - 1
        while i >= 0 and j >= 0 and p1[i] == p2[j]:
            i -= 1
            j -= 1 
        return p1[i + 1]
    def travel(self, root, p, path):
        if not root:
            return False
        if root == p:
            path.append(root)
            return True
        if self.travel(root.left, p, path) or self.travel(root.right, p, path):
            path.append(root)
            return True
        return False