class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if i > 0 and dp[0][i] != 1:
                    break
                if s[i:j] in wordDict:
                    dp[0][j] = 1
        if dp[0][len(s)]:
            return True
        return False     