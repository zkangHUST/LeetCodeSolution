class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, self.check(c)
        while l <= r:
            s = l * l + r * r
            if s == c:
                return True
            if s < c:
                l += 1
            else:
                r -= 1
        return False
    def check(self, num):
        if num == 1 or num == 0:
            return num
        l, r = 1, num // 2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                break
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return mid