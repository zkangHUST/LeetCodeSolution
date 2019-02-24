class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        minx = m
        miny = n
        for v in ops:
            if v[0] < minx:
                minx = v[0]
            if v[1] < miny:
                miny = v[1]
        return minx * miny

# ops = [[2,2],[3,3]]
ops = []
res = Solution()
ans = res.maxCount(3, 3, ops)
print(ans)