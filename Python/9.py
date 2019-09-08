class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        p = str(x)
        i, j = 0, len(p) - 1
        while i < j:
            if p[i] != p[j]:
                return False
            i += 1
            j -= 1
        return True