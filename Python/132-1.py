class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        dp = [0 for i in range(len(s))]
        ispalindrome = [[0 for i in range(len(s))] for j in range(len(s))]
        for j in range(l):
            for i in range(j + 1):
                if s[i] != s[j]:
                    ispalindrome[i][j] = 0
                elif j - i < 2  or ispalindrome[i + 1][j - 1]:
                    ispalindrome[i][j] = 1

        for i in range(len(s)):
            if ispalindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(i):
                    if ispalindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[l - 1]
  

s = Solution()
str = "abcd"
print(s.minCut(str))