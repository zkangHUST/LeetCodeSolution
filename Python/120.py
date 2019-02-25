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
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = Solution()
ans = res.minimumTotal(triangle)
print(ans)

                    


        
