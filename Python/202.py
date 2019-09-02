class Solution:
    def isHappy(self, n: int) -> bool:
        exist = set()
        exist.add(n)
        while n != 1:
            n = self.get(n)
            if n not in exist:
                exist.add(n)
            else:
                return False
        return True
    def get(self, n):
        ans = 0
        while n:
            tmp = n % 10
            ans += tmp * tmp
            n = n // 10
        return ans