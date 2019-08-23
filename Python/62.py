class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        return self.get(m, n, 1, 1)
    def get(self, m, n, i, j):
        if i > m or j > n:
            return 0
        if i == m and j == n - 1:
            return 1
        if j == n and i == m - 1:
            return 1
        return self.get(m, n, i + 1, j) + self.get(m, n, i, j + 1)