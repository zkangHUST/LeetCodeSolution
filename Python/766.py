class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix[0])
        columns = len(matrix)
        i = 0   
        j = 0
        while(i + 1 < rows):
            while(j + 1 < columns):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                j += 1
            j = 0
            i += 1
        return True

# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]

matrix = [
  [1,2],
  [2,2]
]

res = Solution()
ans = res.isToeplitzMatrix(matrix)
print(ans)

