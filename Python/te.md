八皇后问题，是一个古老而著名的问题，是回溯算法的典型案例。该问题是国际西洋棋棋手马克斯·贝瑟尔于1848年提出：在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。 高斯曾经研究过这个问题，他认为有76种方案。1854年在柏林的象棋杂志上不同的作者发表了40种不同的解，后来有人用图论的方法解出92种结果。计算机发明后，解决八皇后的问题就变得非常简单了。
假设八个皇后的位置分别用X1到X8表示，那么Xi可以取的值为1~8，因此，问题的解可以用向量 {x1,x2,x3,x4,x5,x6,x7,x8｝表示，解空间包含8^8个向量。回溯法求解八皇后问题的代码如下，也可以推广至求解N皇后问题。

```
class Solution:
    def __init__(self, n):
        self.tmp = [0] * n
        self.cnt = 0
    def get(self, m, n):
        if (m == n):
            print(self.tmp)
            self.cnt += 1
            return 
        for i in range(n):
            self.tmp[m] = i
            if self.check(m) == True:
                self.get(m + 1, n)
        return
    def check(self, n):
        for i in range(n):
            if self.tmp[i] == self.tmp[n] or abs(self.tmp[i] - self.tmp[n]) == n - i:
                return False
        return True
if __name__ == '__main__':
    res = Solution(8)
    res.get(0, 8)
    print(res.cnt)

```
八个皇后在8x8棋盘上共有16777216种摆放方法，但只有92个互不相同的解。如果将旋转和对称的解归为一种的话，则一共有12个独立解，具体如下：







（图来自维基百科）