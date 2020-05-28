class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # ans = 0
        if n == 0:
            return 1
        ans = 0
        for i in range(n + 1):
            ans += self.get(i)
        return ans 

    def get(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 10
        ans, cnt = 1, 0
        while cnt < n:
            if cnt == 0:
                ans *= 9
            else:
                ans *= 10 - cnt
            cnt += 1
        return ans 
    
