class Solution:
    def rotateString(self, A: str, B: str) -> bool: 
        if A == B:
            return True
        for i in range(len(A)):
            if A[i] == B[0]:
                tmp = A[i:] + A[0:i]
                if tmp == B:
                    return True
        return False
