class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.get(nums, target)
    def get(self, nums, target):
        if target <= 0:
            return 0
        ans = 0
        for val in nums:
            if val == target:
                ans += 1
            else:
                ans += self.get(nums, target - val)
        return ans