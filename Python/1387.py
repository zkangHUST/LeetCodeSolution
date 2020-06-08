class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.weight = {}
        res = [i for i in range(lo, hi + 1)]
        res.sort(key = lambda x:(self.getWeight(x), x))
        return res[k - 1]
    def getWeight(self, n):
        if n in self.weight:
            return self.weight[n]
        if n == 1:
            self.weight[n] = 0
        elif n % 2 == 0:
            self.weight[n] = 1 + self.getWeight(n // 2)
        else:
            self.weight[n] = 1 + self.getWeight(3 * n + 1)
        return self.weight[n]