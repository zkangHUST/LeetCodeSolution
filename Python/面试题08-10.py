class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.dfs(image, sr, sc,image[sr][sc], newColor)
        return image
    def dfs(self, image, sr, sc, oldColor, newColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != oldColor:
            return
        if image[sr][sc] == newColor:
            return
        image[sr][sc] = newColor
        dir = [0, 1, 0, -1, 0]
        for i in range(len(dir) - 1):
            self.dfs(image, sr + dir[i], sc + dir[i + 1], oldColor, newColor)