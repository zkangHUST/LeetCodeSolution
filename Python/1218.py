class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for v in arr:
            if v - difference in dp:
                dp[v] = dp[v - difference] + 1
            else:
                dp[v] = 1
        return max(dp.values())