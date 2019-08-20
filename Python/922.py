class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ret = [0 for i in range(len(A))]
        i, j = 0, 1
        for val in A:
            if val % 2 == 0:
                ret[i] = val
                i += 2
            else:
                ret[j] = val
                j += 2
        return ret