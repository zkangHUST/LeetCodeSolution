# 动态规划
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        dp = [0 for i in range(target + 1)]
        for i in range(target + 1):
            for val in nums:
                if i == val:
                    dp[i] += 1
                elif i > val:
                    dp[i] += dp[i - val]
        return dp[target]