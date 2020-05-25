class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        areas ={0:0}
        color = 1
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    color += 1
                    areas[color] = self.getArea(grid, i, j, rows, cols, color)
                    ans = max(ans, areas[color])
        # print(grid)
        for i in range(rows):
            for j in range(cols):
                s = set()
                if grid[i][j] == 0:
                    val = 1
                    s.add(self.getColor(grid, i + 1, j, rows, cols))
                    s.add(self.getColor(grid, i - 1, j, rows, cols))
                    s.add(self.getColor(grid, i, j + 1, rows, cols))
                    s.add(self.getColor(grid, i, j - 1, rows, cols))
                    # print(s)
                    for v in s:
                        val += areas[v]
                    ans = max(ans, val)
        return ans


    def getColor(self, grid, i, j, rows, cols):
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return 0
        return grid[i][j]

    def getArea(self, grid, i, j, rows, cols, color):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or grid[i][j] > 1:
            return 0
        ans = 1
        grid[i][j] = color
        dire = [0, 1, 0, -1, 0]
        for k in range(len(dire) - 1):
            ans += self.getArea(grid, i + dire[k], j + dire[k + 1], rows, cols, color)
        return ans