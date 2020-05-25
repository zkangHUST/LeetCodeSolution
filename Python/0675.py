class item:
    def __init__(self, x, y, h):
        self.h = h
        self.x = x
        self.y = y

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    it = item(i, j, forest[i][j])
                    trees.append(it)
        trees = sorted(trees, key = lambda it:it.h)
        x, y = 0, 0
        total = 0
        for v in trees:
            steps = self.BFS(forest, x, y, v.x, v.y)
            if steps == -1:
                return -1 
            total += steps
            x, y = v.x, v.y
        return total
    
    def BFS(self, forest, x0, y0, x1, y1):
        rows = len(forest)
        cols = len(forest[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]
        q = [[x0, y0]]
        directions = [0, 1, 0, -1, 0]
        steps = 0
        while len(q) > 0:
            size = len(q)
            while size > 0:
                m, n = q.pop(0)
                size -= 1
                if m == x1 and n == y1:
                    return steps
                for i in range(len(directions) - 1):
                    x = m + directions[i]
                    y = n + directions[i + 1]
                    if x < 0 or y < 0 or x >= rows or y >= cols or visited[x][y] == 1 or forest[x][y] == 0:
                        continue

                    visited[x][y] = 1
                    q.append([x, y])
            steps += 1
        return -1