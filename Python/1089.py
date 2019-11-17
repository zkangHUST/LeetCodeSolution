class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = j = 0
        while j < len(arr):
            if arr[i] != 0:
                j += 1
            else:
                j += 2
            i += 1
        i -= 1
        j = len(arr) - 1
        while i >= 0:
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            arr[j] = arr[i]
            j -= 1
            i -= 1
    
arr = [8,4,5,0,0,0,0,7]
p = Solution()
p.duplicateZeros(arr)
print(arr)