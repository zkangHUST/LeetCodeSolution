class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row , col = len(matrix), len(matrix[0])
        for i in range(row):
            if matrix[i][0] > target or matrix[i][col - 1] < target:
                continue
            l , r = 0, col - 1
            while l <= r:
                mid = l + (r - l) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
