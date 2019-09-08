class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        i, j = 0, 1
        ans = 0
        while j < len(A):
            diff = A[j] - A[i]
            cnt = 2
            j += 1
            while j < len(A):
                if A[j] == A[j - 1] + diff:
                    j += 1
                    cnt += 1
                    if cnt >= 3:
                        ans += (cnt - 3 + 1)
                else:
                    i = j - 1
                    break
        return ans 