class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            flag = True
        else :
            flag = False
        n = abs(n)
        if n % 2 == 0:
            tmp = self.myPow(x, n // 2)
            tmp *= tmp
        else:
            tmp = self.myPow(x, n // 2)
            tmp = tmp * tmp * x
        
        if flag :
            return 1 / tmp
        else:
            return tmp
