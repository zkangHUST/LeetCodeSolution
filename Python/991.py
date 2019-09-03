class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        cnt = 0
        while y != x:
            if y > x:
                if y % 2 == 0:
                    y = y // 2
                else:
                    y += 1
                cnt += 1
            else:
                cnt += x - y
                break
        return cnt
 
x = 9411920
y = 10000009
p = Solution()
ans = p.brokenCalc(x, y)