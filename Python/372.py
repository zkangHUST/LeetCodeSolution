class Solution:
    def superPow(self, a: int, b):
        if len(b) == 1:
            return self.powerMod(a, b[0]) % 1337
        return self.powerMod(self.superPow(a, b[0:-1]), 10) * self.powerMod(a, b[-1]) % 1337
    def powerMod(self, a, b):
        res = 1
        while b > 0:
            res = res * a % 1337
            b -= 1
        return res
        
res = Solution()
ans = res.superPow(2, [3])
print(ans)