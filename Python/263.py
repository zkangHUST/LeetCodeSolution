class Solution:
    def isUgly(self, num: int) -> bool:
        while num:
            if num == 1:
                return 1
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False