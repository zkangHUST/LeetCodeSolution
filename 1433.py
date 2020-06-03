class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        return self.check(s1, s2) or self.check(s2, s1)
    
    def check(self,a, b):
        for i in range(len(a)):
            if a[i] < b[i]:
                return False
        return True
