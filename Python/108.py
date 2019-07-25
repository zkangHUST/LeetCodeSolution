class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        r = TreeNode(0)
        mid = len(nums) // 2
        r.val = nums[mid]
        r.left = self.sortedArrayToBST(nums[:mid])
        r.right = self.sortedArrayToBST(nums[mid + 1:])
        return r
