class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if (not A) or len(A) == 1 :
            return True
        flag = 0
        for i in range(len(A) - 1):
            if (A[i] < A[i + 1]):
                if (flag == 2):
                    return False
                else:
                    flag = 1
            elif A[i] > A[i + 1]:
                if (flag == 1):
                    return False
                else:
                    flag = 2
        return True