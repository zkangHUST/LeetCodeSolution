class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.cnt = 0
        self.dfs(0, target, 0, d, f)
        return self.cnt
    
    def dfs(self, cur, target, num, sum, f):
        if cur == target and num == sum:
            self.cnt += 1
            return
        if cur > target or num == sum:
            return 
        if cur + (sum - num) * f < target:
            return
        for i in range(1, f + 1):
            self.dfs(cur + i, target, num + 1, sum, f)
        