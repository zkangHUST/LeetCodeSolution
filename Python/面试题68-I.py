# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1 找出两条路径,挨个对比,第一个不一样的节点的上一个节点即为最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1, path2 = [], []
        self.getPath(root, p, path1)
        self.getPath(root, q, path2)
        if len(path1) > len(path2):
            path1, path2 = path2, path1
        for i in range(len(path1)):
            if path1[i] != path2[i]:
                return path1[i - 1]
        return path1[-1]
    def getPath(self, root, p, path):
        if root == p:
            path.append(p)
            return 
        if not root:
            return
        path.append(root)
        if root.val < p.val:
            self.getPath(root.right, p, path)
        else: 
            self.getPath(root.left, p, path)

# 解法2 递归求解
# 1. 如果root.val 在p.val 和q.val之间,那么root即为最近公共祖先
# 2. 如果p.val > root.val 且q.val > root.val, 那么向右子树找最近公共祖先
# 3. 如果p.val < root.val 且q.val < root.val, 那么向左子树找最近公共祖先

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root