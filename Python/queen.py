class Solution:
    def __init__(self, n):
        self.tmp = [0] * n
        self.cnt = 0
    def get(self, m, n):
        if (m == n):
            print(self.tmp)
            self.cnt += 1
            return 
        for i in range(n):
            self.tmp[m] = i
            if self.check(m) == True:
                self.get(m + 1, n)
        return
    def check(self, n):
        for i in range(n):
            if self.tmp[i] == self.tmp[n] or abs(self.tmp[i] - self.tmp[n]) == n - i:
                return False
        return True
if __name__ == '__main__':
    res = Solution(8)
    res.get(0, 8)
    print(res.cnt)

