class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        l = len(s) + 1
        dp = [0 for i in range(l)]
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if s[i] == '*':
                if s[i - 1] == '1':
                    dp[i + 1] == dp[i] * 9 + dp[i - 1] * 9
                elif s[i - 1] == '2':
                    dp[i + 1] += dp[i] * 9 + dp[i - 1] *6
                elif s[i - 1] == '0':
                    dp[i + 1] = dp[i] * 9
                elif s[i - 1] == '*':
                    dp[i + 1] = dp[i] * 9 + dp[i - 1] * 15  
                else:
                    dp[i + 1] = dp[i] * 9
            elif s[i] == '0':
                if s[i - 1] == '*':
                    dp[i + 1] = dp[i - 1] * 2
                elif s[i - 1] > '2' or s[i - 1] == '0':
                    return 0
                else:
                    dp[i + 1] = dp[i - 1]
            else:
                if s[i - 1] == '*':
                    if s[i] <= 6:
                        dp[i + 1] = dp[i] + dp[i - 1] * 2
                    else:
                        dp[i + 1] = dp[i] + dp[i - 1]
                elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= 6):
                        dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[len(s)]

