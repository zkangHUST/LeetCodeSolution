class Solution:
    def minSteps(self, n: int) -> int:
        cnt = 0
        while n != 1:
            n, m = self.get(n)
            cnt += m
        return cnt
    
    def get(self, n):
        for i in range(2, n):
            if n % i == 0:
                return n // i, i
        return 1, n

p = Solution()
p.minSteps(100)