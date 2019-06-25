# 二分查找，区间左闭右开
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles) + 1
        while l < r:
            mid = l  + (r - l) // 2
            if self.hours(piles, mid) <= H:
                r = mid
            else: 
                l = mid + 1
        return l
                
    def hours(self, piles, n):
        h = 0
        for val in piles:
            h += (val + n - 1) // n 
        return h