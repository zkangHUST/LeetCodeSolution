class Solution:
    def imageSmoother(self, M):
        if not M:
            return []
        tmp = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        print(tmp)
        for i in range(len(M)):
            for j in range(len(M[0])):
                tmp[i][j] = self.getXY(M, i, j)
        return tmp
    def getXY(self, M, x, y):
        ans = 0
        cnt = 0
        rows = len(M)
        cols = len(M[0])
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i >= 0 and i < rows and j >= 0 and j < cols):
                    ans += M[i][j]
                    cnt += 1
        return ans // cnt   
res = Solution()
ans = res.imageSmoother([])
print(ans)                 
