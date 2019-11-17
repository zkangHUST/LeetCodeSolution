class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        for i in range(len(s)):
            if s[i] in m:
                if m[s[i]] != t[i]:
                    return False
            else:
                for key in m:
                    if m[key] == t[i]:
                        return False
                m[s[i]] = t[i]
        return True

p = Solution()
a = "abba"
b = "dog cat cat dog"

print(p.wordPattern(a, b))