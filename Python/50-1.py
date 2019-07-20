# 大神的写法
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1 / self.myPow(x, -n)
        else:
            if n % 2 == 0:
                return self.myPow(x * x, n // 2)
            else:
                return x * self.myPow(x * x, n // 2)
