import math
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        cnt = 0
        primenum = [2, 3, 5, 7, 11, 13, 17,19]
        for i in range(L, R + 1):
            n = self.countBits(i)
            if n in primenum:
                cnt+=1
        return cnt
    def isPrime(self, n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        for i in range(2, int(math.sqrt(n)+1)):
            if n%i == 0:
                return False
        return True
    def countBits(self, n):
        return bin(n).count('1')


res = Solution()
l = res.countPrimeSetBits(6,10)
print(l)