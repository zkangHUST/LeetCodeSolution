class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if self.check(s[i + 1:j + 1]) or self.check(s[i:j]):
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True
    def check(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
