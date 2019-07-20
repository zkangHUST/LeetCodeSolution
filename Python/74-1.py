# 首选按照行二分查找，然后按照列二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row
        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][col - 1]:
                m = mid
                l, r = 0, col
                while l < r:
                    mid = l + (r - l) // 2
                    if matrix[m][mid] == target:
                        return True
                    if target < matrix[m][mid]:
                        r = mid
                    else:
                        l = mid + 1
            elif target > matrix[mid][col - 1]:
                l = mid + 1
            else:
                r = mid
        return False