class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        for i in range(len(haystack)-length + 1):
            if haystack[i:i + length] == needle:
                return i   
        return -1
res = Solution()
ans = res.strStr("", "")
print(ans)

