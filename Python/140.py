# 回溯法,超时
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        path = ""
        self.dfs(s, 0, wordDict, path)
        return self.ans
    
    def dfs(self, s, p, wordDict, path):
        if p == len(s):
            # self.ans = True
            self.ans.append(path[:])
            return 
        for i in range(p, len(s)):
            if s[p:i + 1] in wordDict:
                if not path:
                    tmp = path + s[p:i + 1]
                else:
                    tmp = path + " " + s[p:i + 1]
                self.dfs(s, i + 1, wordDict, tmp)