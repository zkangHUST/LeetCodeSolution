class Solution:
    def shipWithinDays(self, weights, D):
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = l + (r - l) // 2
            m = self.check(weights, D, mid)
            n = self.check(weights, D, mid - 1)
            if m and not n:
                return mid 
            if m:
                r = mid - 1
            else:
                l = mid + 1

            
    def check(self, weights, D, c):
        if c < max(weights):
            return False
        i = 0
        w = 0
        cnt = 0
        while i < len(weights):
            if w < c:
                w += weights[i]
                i += 1
            else:
                if w > c:
                    i -= 1
                w  = 0
                cnt += 1
        if w > c:
            cnt += 2
        if 0 < w < c:
            cnt += 1
        if cnt <= D:
            return True
        else:
            return False
l = [1,2,3,1,1]
# ,4,5,6,7,8,9,10]

res = Solution()
ans = res.shipWithinDays(l, 4)
print(ans)