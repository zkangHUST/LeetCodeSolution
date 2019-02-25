Triangle
这道题也是来源于Leetcode,题目英文描述如下，比较简单，就不翻译了。

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to **adjacent numbers** on the row below.

For example, given the following triangle
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
**Note:**
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

这也是一道考察动态规划的基础题目。首先要搞清楚的是何为adjacent numbers。在这个题目里面，对于处于(i,j)位置处的数字，上一层中(i-1,j)和(i-1,j-1)是它的adjacent numbers，下一层中，(i+1,j)和(i+1, j+1)也是它的adjacent numbers。

下面我们来简单分析一下解决这个题目的思路，如果把从(0,0)走到(i, j)位置处的最短路径和定义为f(i,j)，那么很显然f(0,0) = triangle[0][0]。题目要求只能从一个点移动到下一层的adjacemt number。那么要从(0,0)走到(i, j)，必须先从(0,0)走到(i-1,j)位置或者(i-1,j-1)位置。要想走到(i,j)处的路径和最短，那么走到(i-1,j)或者(i-1, j-1)位置处的路径和也必须为最短。因此，f(i, j) = min{f(i-1,j), f(i-1,j-1)} + triangle[i][j]。同时我们应该注意到在边界处的特殊情况，当j == 0时，想走到(i, 0)只能从(i-1,0)走,只有唯一一条路径，因此f(i, 0) = f(i-1, 0) + triangle[i][0]；当j == len(triangle[i])-1时，想走到(i,j)只能从(i-1,j-1)走，也只有一条路径，因此f(i,j)=f(i-1,j-1)+triangle[i][j]。总结一下上述分析就是:

根据上面的分析那么可以写出代码:
```
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        for i in range(1, rows):
            for j in range(len(triangle[i])):
                if (j == 0):
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif (j == len(triangle[i - 1])):
                    triangle[i][j] = triangle[i - 1][j -1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j]
        ans = min(triangle[-1])
        return ans
```
代码实现稍微做了一下变形，采用自底向上的计算方法，避免递归调用。