class Solution:
    def isUnique(self, astr: str) -> bool:
        chars = set()
        for c in astr:
            if c in chars:
                return False
            chars.add(c)
        return True
                