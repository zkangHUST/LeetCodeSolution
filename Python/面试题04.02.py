# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.tree(nums, 0, len(nums) - 1)

    def tree(self, nums, i, j):
        if i > j :
            return None
        if i == j:
            r = TreeNode(nums[i])
            return r
        mid = (i + j) // 2
        r = TreeNode(nums[mid])
        r.left = self.tree(nums, i, mid - 1)
        r.right = self.tree(nums, mid + 1, j)
        return r