class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a, b, c = 1, 1, 0
        ans = 0
        for i in range(3, n + 1):
            ans = a + b + c
            c, b, a = b, a, ans 
        return ans