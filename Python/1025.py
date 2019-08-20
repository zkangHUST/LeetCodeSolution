class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = {}
        dp[1] = False
        dp[2] = True
        for i in range(3, N + 1):
            dp[i] = False
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break
        return dp[N]