class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        target = sum(A) // 3
        tmp, cnt = 0, 0
        for i in range(len(A)):
            tmp += A[i]
            if tmp == target:
                tmp = 0
                cnt += 1
        if cnt != 3:
            return False
        return True