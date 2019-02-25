
Leetcode上面有一道题目，很有意思。题目描述是这样的：
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。注意：每次只能向下或者向右移动一步。

**Example**
```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```
我们来分析一下。假设我们从(0,0)开始沿某一条路径到达位置(i,j)处，获得最小的和。我们把这个和记为f(i,j)。那么针对f(i,j)有下面两条规则
1. 首先，如果i,j均为0的话，那么显然f(0,0) = grid[0][0]
2. 因为题目规定，路径只能向右或者向下。那么想要到达（i,j）这个位置，必须先到达(i-1，j)处或者（i, j-1）处。因此到达（i,j）的最小路径和应该是f(i,j) = min{f(i -1, j), f(i, j - 1 )} + grid[i][j]
基于这两条规则，我们可以写出代码

```
class Solution():
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        # 防止输入grid == []
        if (row == 0):
            return 0    
        # 防止输入grid == [[]]
        colum = len(grid[0])
        if (row == 0 or colum == 0):
            return 0
        res = [[0 for i in range(colum)] for j in range(row)] 
        for i in range(row):
            for j in range(colum):
                if (i == 0 and j == 0):
                    res[i][j] = grid[0][0]
                else:
                    if i == 0:
                        res[i][j] = res[i][j - 1] + grid[i][j]
                    elif j == 0:
                        res[i][j] = res[i - 1][j] + grid[i][j]
                    else:
                        res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[row - 1][colum - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
res = Solution()
ans = res.minPathSum(grid)
```
在这段代码当中，我们初始化了一个跟grid维度一样的二维列表，用这个列表来记录到达(i,j)位置的最小路径和。事实上，直接在原来的grid列表中记录就可以了，完全没有必要申请这样一个列表，这样可以大幅提高速度，同时节省内存空间。这个在当时刷题时没有想到。那么我们可以把代码改进一下


```
class Solution():
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if (row == 0):
            return 0    
        colum = len(grid[0])
        if (row == 0 or colum == 0):
            return 0 
        for i in range(row):
            for j in range(colum):
                if (i == 0 and j == 0):
                    continue
                else:
                    if i == 0:
                        grid[i][j] = grid[i][j - 1] + grid[i][j]
                    elif j == 0:
                        grid[i][j] = grid[i - 1][j] + grid[i][j]
                    else:
                        grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[row - 1][colum - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
res = Solution()
ans = res.minPathSum(grid)
print(ans);        
```


人生路有很多条,请务必选择一条适合自己的并且坚持下去!