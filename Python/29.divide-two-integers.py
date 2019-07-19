#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend * divisor < 0):
            flag = -1
        else:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        left = 0
        right = dividend + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * divisor <= dividend and (mid + 1) * divisor > dividend :
                break
            if mid * divisor > dividend:
                right = mid
            else:
                left = mid  + 1
        mid *= flag
        # handle overflow
        if mid >  2147483647:
            mid = 2147483647
        return mid
        
if __name__ == "__main__":
    res = Solution()
    ans = res.divide(7, -3)
    print(ans)

