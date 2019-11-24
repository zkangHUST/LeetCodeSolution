class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0:
            return False 
        if num == 1 :
            return True
        if num % 4 != 0:
            return False
        return self.isPowerOfFour(num // 4)