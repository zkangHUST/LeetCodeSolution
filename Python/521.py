class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        i = 0
        j = 0
        length = -1
        while(i < len(strs)):
            while(j < len(strs)):
                if (j == i):
                    j += 1
                    continue
                flag = self.isSubStr(strs[j], strs[i]) 
                if (flag):
                    break
                j += 1   
            if (flag == 0 and length < len(strs[i])):
                length = len(strs[i])
            i += 1
            j = 0
            flag = 0
        return length
    def isSubStr(self, a, b):
        if (a == b):
            return True
        if (len(b)>=len(a)):
            return False
        i = 0
        j = 0
        while(i < len(a) and j < len(b)):
            if a[i] == b[j]:
                j += 1
            i += 1
        if (j == len(b)):
            return True
        return False
res = Solution()
l= ["aba","gahbia","gahbia","abcdef","abcdef"]
ans = res.findLUSlength(l)
print(ans)
