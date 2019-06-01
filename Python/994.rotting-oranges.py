#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# bfs的应用
# 1. 找出所有腐烂的橘子放入队列
# 2. 对队列中现存的每个橘子(不算新加入的)污染其周围的橘子，污染成功，标志位置为True，并将新污染的橘子放入队列。
# 3. 检查标志位是否为true，是则cnt加1。
# 4. 重复步骤2，直至队列为空。
# 5. 检查还有没有没被污染的橘子(因为有的橘子永远不会被污染)
# 6. 返回cnt或-1.

# orangesRotting
#     q = queue()
#     cnt = 0
#     flag = False
#     # 1. 找出所有的腐烂橘子放入队列
#     for orange u in grid:
#         if u == 2  // rotten orange
#             q.put(u)
#     while (not q.empty()):
#         size = q.size()
#         for i in [0, size)
#             u = q.pop()
#             for v in u.neighbor
#                 if v == 1:
#                     v = 2
#                     flag = True
#                     q.put(v)
#         if flag
#             cnt += 1
#             flag = False
#     for u in grid:
#         if u == 1:
#             return -1
#     return cnt
        
from queue import Queue
class orange:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getXY(self):
        return self.x, self.y
class Solution:
    def __init__(self):
        self.posx = [-1, 1, 0, 0]
        self.posy = [0, 0, -1, 1] 
    def orangesRotting(self, grid):
        cnt = 0
        flag = False
        q = Queue()
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if (grid[i][j] == 2):
                    r = orange(i, j)
                    q.put(r)
        while(not q.empty()):
            size = q.qsize()
            for i in range(size):
                cur = q.get()
                x, y = cur.getXY()
                for j in range(4):
                    if (x + self.posx[j] < 0 or x + self.posx[j] >= row or 
                        y + self.posy[j] < 0 or y + self.posy[j] >= col or
                        grid[x + self.posx[j]][y + self.posy[j]] != 1):
                        continue
                    else:
                        flag = True
                        grid[x + self.posx[j]][y + self.posy[j]] = 2
                        r = orange(x + self.posx[j], y + self.posy[j])
                        q.put(r)
            if (flag):
                cnt += 1    
                flag = False
        for i in range(row):
            for j in range(col):
                if (grid[i][j] == 1):
                    return -1
        return cnt






        


