class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        x = [v[0] for v in ops]
        y = [v[1] for v in ops]
        if (x and y):
            return min(x) * min(y)
        return m * n
# ops = [[2,2],[3,3]]
ops = []
res = Solution()
ans = res.maxCount(3, 3, ops)
print(ans)