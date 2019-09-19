class Solution:
    def wordBreak(self, s: str, wordDict):
        if not s:
            return False
        self.ans = False
        self.dfs(s, 0, wordDict)
        return self.ans
    def dfs(self, s, p, wordDict):
        if p == len(s):
            self.ans = True
            return 
        for i in range(p, len(s)):
            if self.ans:
                return
            if s[p:i + 1] in wordDict:
                self.dfs(s, i + 1, wordDict)

s = "leetcode"
wordlist = ["leet", "code"]
p = Solution()
print(p.wordBreak(s, wordlist))


        