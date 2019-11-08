class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt, l, r = 0, 0, 0
        for c in s:
            if c == 'L':
                l += 1
            elif c == 'R':
                r += 1
            if l == r:
                cnt += 1
                l = r = 0
        return cnt