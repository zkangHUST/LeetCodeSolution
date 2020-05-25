class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        if n == 3:
            return 4
        # if n == 
        x, y, z = 1, 2, 4
        s = 0
        for i in range(4, n + 1):
            s = (x + y + z) % 1000000007
            x, y, z = y, z, s
        return s
