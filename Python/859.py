class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        # if A == B:
        #     for a in A:
        #         if A.count(a) > 2:
        #             return True
        #     return False
        if A == B:
            if len(A) != len(set(A)):
                return True
            return False
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)
        if len(diff) != 2:
            return False
        if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True
        return False