class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    ans.append(self.dfs(land, i, j))
        return sorted(ans)
    def dfs(self, land, x, y):
        if x < 0 or x >= len(land) or y < 0 or y >= len(land[0]):
            return 0
        if land[x][y]:
            return 0
        land[x][y] = 1
        ans = 1
        # dir = [0, 1, 0, -1, ]
        ans += self.dfs(land, x, y + 1)
        ans += self.dfs(land, x, y - 1)
        ans += self.dfs(land, x - 1, y)
        ans += self.dfs(land, x + 1, y)
        ans += self.dfs(land, x - 1, y - 1)
        ans += self.dfs(land, x - 1, y + 1)
        ans += self.dfs(land, x + 1, y - 1)
        ans += self.dfs(land, x + 1, y + 1)
        return ans 
