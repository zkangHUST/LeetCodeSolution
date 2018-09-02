class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        index = 0
        cnt =0
        for i in range(len(g)):
            for j in range(index, len(s)):
                if(s[j]<g[i]):
                    continue
                else:
                    s.remove(s[j])
                    index = j
                    cnt+=1
                    break
        return cnt


res = Solution()
g=[3,2,1]
s=[3,2,1]
ans= res.findContentChildren(g,s)
print(ans)

