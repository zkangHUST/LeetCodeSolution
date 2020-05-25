class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        i, j, k = 0, 0, 0
        pos = [0, 1, 0, -1, 0]
        num = 1
        while num <= n ** 2:
            matrix[i][j] = num
            num += 1
            x, y = i + pos[k], j + pos[k + 1]
            if x < 0 or x >= n or y < 0 or y >= n or matrix[x][y] != 0:
                k = (k + 1) % 4
            i += pos[k]
            j += pos[k + 1]
        return matrix
        