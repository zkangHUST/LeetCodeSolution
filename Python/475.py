# 超时了
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l = 0
        r = max(houses) + max(heaters)
        while l <= r:
            mid = l + (r - l) // 2
            m = self.check(houses, heaters, mid)
            n = self.check(houses, heaters, mid - 1)
            if m and not n:
                return mid
            if m :
                r = mid - 1
            else:
                l = mid + 1


    def check(self, houses, heaters, r):
        if r < 0:
            return False
        flag = False
        for val in houses:
            for h in heaters:
                if h - r <= val <= h + r:
                    flag = True
                    break
            if not flag:
                return False
            flag = False
        return True 
        
