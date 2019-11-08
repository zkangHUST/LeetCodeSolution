class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [l for i in range(l)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(1, nums[i]):
                if i + j < len(dp) and dp[i] + 1 < dp[i + j]:
                    dp[i + j] = dp[i] + 1
        return dp[-1]
                     