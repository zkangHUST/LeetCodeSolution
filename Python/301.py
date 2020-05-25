class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        cnt = self.getCnts(s)
        path = ""
        self.bfs(s, path, 0, 0, cnt, ans);
        return ans
    def bfs(self, s, path, i, nums, cnt, ans):
        if nums == cnt:
            path = path + s[i:]
            if self.getCnts(path) == 0 and path not in ans:
                ans.append(path)
            return
        if i >= len(s):
            return
        self.bfs(s, path + s[i], i + 1, nums, cnt, ans)
        if s[i] == '(' or s[i] == ')':
            self.bfs(s, path, i + 1, nums + 1, cnt, ans)


    def getCnts(self, path):
        cntleft = 0
        cntright = 0
        for c in path:
            if c == '(':
                cntleft += 1
            elif c == ')':
                if cntleft > 0:
                    cntleft -= 1
                else:
                    cntright += 1
        return cntleft + cntright