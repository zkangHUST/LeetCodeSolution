class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return None
        return self.tree(1, n)
    def tree(self, l, r):
        if l > r:
            return [None]
        if r == l:
            return [TreeNode(l)]
        ans = []
        for i in range(l, r + 1):
            for lc in self.tree(l, i - 1):
                for rc in self.tree(i + 1, r):
                    root = TreeNode(i)
                    root.left = lc
                    root.right = rc
                    ans.append(root)
        return ans