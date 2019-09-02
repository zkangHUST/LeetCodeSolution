# 超时
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.ans = ""
        self.cnt = 0
        path = ""
        nums = [str(i) for i in range(1, n + 1)]
        self.dfs(n, 0, nums, path, k)
        return self.ans
    def dfs(self, n, cnt, nums,path, k):
        if self.cnt == k:
            return 
        if cnt == n:
            self.ans = path
            self.cnt += 1
            return
        for c in nums:
            if c not in path:
                self.dfs(n, cnt + 1, nums, path + c, k)
p = Solution()
print(p.getPermutation(9, 331987))