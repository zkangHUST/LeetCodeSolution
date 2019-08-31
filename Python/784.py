class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        path = ""
        self.ans = []
        self.dfs(S, 0, path)
        return self.ans
    def dfs(self, S, cnt, path):
        if cnt == len(S):
            if path not in self.ans:
                self.ans.append(path)
            return 
        if S[cnt].islower():
            self.dfs(S, cnt + 1, path + S[cnt].upper())
        if S[cnt].isupper():
            self.dfs(S, cnt + 1, path + S[cnt].lower())
        self.dfs(S, cnt + 1, path + S[cnt])