class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    pos.append([i, j])
        for p in pos:
            for i in range(len(matrix)):
                matrix[i][p[1]] = 0
            for j in range(len(matrix)):
                matrix[p[0]][j] = 0
        