class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    q.append(i * cols + j)
                else:
                    matrix[i][j] = float("inf")
        dirction = [0, 1, 0, -1, 0]
        while len(q) > 0:
            top = q.pop(0)
            for k in range(len(dirction) - 1):
                x = top // cols + dirction[k]
                y = top % cols + dirction[k + 1]
                if x >= 0 and x < rows and y >= 0 and y < cols \
                    and matrix[x][y] > matrix[top // cols][top % cols] + 1:
                    matrix[x][y] = matrix[top // cols][top % cols] + 1
                    q.append(x * cols + y)
        return matrix