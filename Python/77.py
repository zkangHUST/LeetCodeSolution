class Solution:
    def combine(self, n, k):
        self.tmp = []
        self.result = []
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.trace(n,1, k, 1)
        return self.result
    def trace(self, m, n, k, start):
        if (n > k) :
            self.result.append(self.tmp[:])
            return
        for i in range(start, m + 1):
            if (self.tmp and i > self.tmp[-1]) or not self.tmp:
                self.tmp.append(i)
                self.trace(m, n + 1, k, i + 1)
                self.tmp.remove(i)

res = Solution()
l = res.combine(20,16)
print(l)
