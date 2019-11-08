class Solution:
    def longestPalindrome(self, s: str) -> str:
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
        maxlen = 0
        ans = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j]:
                    if j - i + 1 > maxlen:
                        maxlen = j - i + 1
                        ans = s[i:j+1]
        return ans