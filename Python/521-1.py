def lens(str):
        return len(str)
class Solution:
    
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        l = set()
        strs = sorted(strs, key = lens, reverse = True)
        i = 0
        while(i < len(strs) - 1):
            if len(strs[i]) > len(strs[i+1]):
                if (self.substr(l, strs[i])):
                    l.add(strs[i])
                else:
                    return len(strs[i])
            else:
                l.add(strs[i])
            i += 1
        if (self.substr(l,strs[i])):
            return -1
        return len(strs[i])
    def substr(self, s,k):
        for v in s:
            if self.check(k, v):
                return True
        return False
    def check(self, a, b):
        if (len(a) > len(b)):
            return False
        if (len(a) == len(b) and a != b):
            return False
        if (a == b):
            return True
        i = 0
        j = 0
        while(i < len(a) and j < len(b)):
            if a[i] == b[j]:
                i += 1
            j += 1
        if (i != len(a)):
            return False
        return True
res = Solution()
l = ["aabbcc", "aabbcc","cb"]
ans = res.findLUSlength(l)
print(ans)
