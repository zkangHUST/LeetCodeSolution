# 最小堆
import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(l, -matrix[i][j])
                if len(l) > k:
                    heapq.heappop(l)
        return -l[0]

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

res = Solution()
ans = res.kthSmallest(matrix, 8)
print(ans)