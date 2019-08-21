class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 and K == 1:
            return 0
        if K % 2 == 0:
            return 1 - self.kthGrammar(N - 1, K / 2)
        else:
            return self.kthGrammar(N - 1, (K + 1) / 2)