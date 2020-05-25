class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        l = len(s) + 1
        dp = [0 for i in range(l)]
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                dp[i + 1] = dp[i - 1]
            elif s[i] == '0':
                return 0
            if s[i] != '0':
                dp[i + 1] += dp[i]
        return dp[len(s)]

