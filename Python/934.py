class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
        found = False
        q = []
        for i in range(rows):
            if found:
                break;
            for j in range(cols):
                if A[i][j] == 1:
                    m, n = i, j
                    found = True
                    break
        self.dfs(A, m, n, rows, cols, q)
        # print(q)
        return self.bfs(A, rows, cols,q)

    def dfs(self, A, x, y, rows, cols, q):
        if x < 0 or  x >= rows or y < 0 or y >= cols:
            return
        if A[x][y] == 0 or A[x][y] == 2:
            return
        A[x][y] = 2
        q.append([x, y])
        direction = [0, 1, 0, -1, 0]
        for i in range(len(direction) - 1):
            self.dfs(A, x + direction[i], y + direction[i + 1], rows, cols, q)

    def bfs(self, A, rows, cols, q):
        steps = 0
        direction = [0, 1, 0, -1, 0]
        while len(q) > 0:
            nums = len(q)
            while nums > 0:
                top = q.pop(0)
                nums -= 1
                x, y = top[0], top[1]
                for i in range(len(direction) - 1):
                    m, n = x + direction[i], y + direction[i + 1] 
                    if m < 0 or m >= rows or n < 0 or n >= cols or A[m][n] == 2:
                        continue
                    if A[m][n] == 1:
                        return steps
                    A[m][n] = 2
                    q.append([m, n])
            steps += 1
        return -1