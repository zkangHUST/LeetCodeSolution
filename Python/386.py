class Solution:
    def lexicalOrder(self, n):
        self.ans = []
        self.dfs(n, 0)
        return self.ans
    def dfs(self, n, num):
        if num > n:
            return False
        elif num != 0:
            self.ans.append(num)
        for i in range(0, 10):
            if num == 0 and i ==0:
                continue
            if not self.dfs(n, num * 10 + i):
                break
        return True

p = Solution()
print(p.lexicalOrder(13))
