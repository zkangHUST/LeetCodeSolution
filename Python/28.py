class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1
        i = j = 0
        if(len(needle) == 0):
            return 0
        while(i < len(haystack) and j <len(needle)):
            if (haystack[i] != needle[j]):
                if (index != -1):
                    i = index
                index = -1
                j = 0
            else:
                if (j == 0):
                    index = i
            
                j += 1
            i += 1
        if (j == len(needle)):
            return index
        else:
            return -1
res = Solution()
ans = res.strStr("helloworld", "ow")
print(ans)

