class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        m = {}
        l = str.split(" ")
        if len(pattern) != len(l):
            return False
        print(l)
        for i in range(len(pattern)):
            if pattern[i] in m:
                if m[pattern[i]] != l[i]:
                    return False
            else:
                for key in m:
                    if m[key] == l[i]:
                        return False
                m[pattern[i]] = l[i]
        return True

p = Solution()
a = "abba"
b = "dog cat cat dog"

print(p.wordPattern(a, b))