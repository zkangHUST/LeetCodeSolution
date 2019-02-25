class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        res = []
        for j in range(rowIndex + 1):
            res.append(self.getnum(rowIndex, j))
        return res
    def getNextRow(self, s):
        
    def getnum(self, i, j):
        if (j == 0 or i == j):
            return 1
        else:
            return self.getnum(i - 1, j - 1) + self.getnum(i - 1, j)
res = Solution()
ans = res.getRow(25)
print(ans)