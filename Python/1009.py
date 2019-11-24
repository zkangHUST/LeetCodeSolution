class Solution:
    def bitwiseComplement(self, N: int) -> int:
        src = bin(N)
        ans = 0
        for c in src[2:]:
            if c == '1':
                ans *= 2
            else:
                ans = ans * 2 + 1
        return ans