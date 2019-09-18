class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.get(nums[:-1]), self.get(nums[1:]))
    def get(self, nums):
        last = now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now