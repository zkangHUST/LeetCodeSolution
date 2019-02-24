
class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        elif root.val == L:
            root.left = None
            root.right = self.trimBST(root.right, L, R)
            return root
        elif root.val == R:
            root.right = None
            root.left = self.trimBST(root.left, L, R)
            return root
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root




