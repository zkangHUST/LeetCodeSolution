class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        m = set()
        for val in A:
            if val in m:
                return val
            else:
                m.add(val)