class Solution:
    def shipWithinDays(self, weights, D):
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = l + (r - l) // 2
            m = self.check(weights, mid)
            n = self.check(weights, mid - 1)
            if m <= D and n > D:
                return mid
            if m > D:
                l = mid + 1
            else:
                r = mid - 1
    def check(self, weights, c):
        if c < max(weights):
            return float("inf")
        tmp = c
        cnt = 0
        for val in weights:
            tmp -= val
            if tmp < 0:
                cnt += 1
                tmp = c - val
        if tmp < 0:
            cnt += 2
        else:
            cnt += 1
        return cnt
# l = [1,2,3,1,1]
l = [1,2,3,4,5,6,7,8,9,10]

res = Solution()
ans = res.shipWithinDays(l, 5)
print(ans)