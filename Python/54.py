class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        pos = [0, 1, 0, -1, 0]
        visited = [[0 for i in range(cols)] for j in range(rows)]
        i, j, k = 0, 0, 0
        ans = []
        while True:
            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] == 1:
                break
            ans.append(matrix[i][j])
            # visited.add(i * rows + j)  
            visited[i][j] = 1
            x, y = i + pos[k], j + pos[k + 1]
            if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] == 1:
                k = (k + 1) % 4
            i = i + pos[k]
            j = j + pos[k + 1]
        return ans

        
