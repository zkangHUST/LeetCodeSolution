class Solution:
    def binaryGap(self, N: 'int') -> 'int':
        s = str(bin(N))
        start = -1
        maxLen = 0
        for i in range(len(s)):
            if s[i] == '1':
                if start != -1 and i - start > maxLen:
                        maxLen = i - start
                start = i
        return maxLen
res = Solution()
ans = res.binaryGap(22)
print(ans)            

