class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] != s[j]:
                        dp[i][j] = 0
                    elif j - i <= 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
        cnt = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j]:
                    cnt += 1
        return cnt
