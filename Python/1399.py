class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = {}
        for i in range(1, n + 1):
            key = self.get(i)
            if key not in cnt:
                cnt[key] = 1
            else:
                cnt[key] += 1
        maxValue = 0
        for v in cnt.values():
            maxValue = max(maxValue, v)
        ans = 0
        for v in cnt.values():
            if v == maxValue:
                ans += 1
        return ans
    def get(self,n):
        ans = 0
        while n:
            ans += n % 10
            n = n // 10
        return ans
