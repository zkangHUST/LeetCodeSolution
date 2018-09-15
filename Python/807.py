class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        left = []
        top = []
        res = 0
        self.view(grid, left, top)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    res +=  min(top[j], left[i]) - grid[i][j]
        return res

    def view(self,grid, leftview, topview):
        leftview.clear()
        topview.clear()
        leftview[:] =[max(v) for v in grid]
        topview[:]= [max(v) for v in zip(*grid)]
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
res = Solution()
ans = res.maxIncreaseKeepingSkyline(grid)
        


        