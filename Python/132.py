class Solution:
    def minCut(self, s: str) -> int:
        self.ret = -1
        self.dfs(s, 0, len(s), 0)
        return self.ret
    def dfs(self, s, start, end, ans):
        if start == end:
            if self.ret == -1:
                self.ret = ans - 1
            else:
                self.ret = min(self.ret, ans - 1)
            return
        for i in range(start + 1, end + 1):
            if self.check(s[start:i]):
                self.dfs(s, i, end, ans + 1)
            
    def check(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            

s = Solution()
str = "ababababababababababababcbabababababababababababa"
print(s.minCut(str))