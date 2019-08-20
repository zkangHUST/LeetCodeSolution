class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        res = [[0 for i in range(row)] for j in range(col)]
        for i in range(row):
            for j in range(col):
                res[j][i] = A[i][j]
        return res