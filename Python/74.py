class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            if target <= matrix[i][col - 1]:
                break
        l, r = 0, col
        while l < r:
            mid = l + (r - l) // 2
            if matrix[i][mid] == target:
                return True
            if target < matrix[i][mid]:
                r = mid
            else:
                l = mid + 1
        return False