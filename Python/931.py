# dfs超时
import math
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        self.ans = math.inf
        for j in range(len(A[0])):
            self.dfs(A, 0, j, 0)
        return self.ans
    
    def dfs(self, A, i, j, sum):
        if i == len(A):
            self.ans = min(self.ans, sum)
            return 
        if j - 1 >= 0:
            self.dfs(A, i + 1, j - 1, sum + A[i][j - 1])
        if j >= 0 and j <= len(A[0]):
            self.dfs(A, i + 1, j, sum + A[i][j])
        if j + 1 < len(A[0]):
            self.dfs(A, i + 1, j + 1, sum + A[i][j + 1])
    