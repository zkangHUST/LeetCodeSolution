class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = list(S)
        t = list(T)
        s=self.delete(s) 
        t=self.delete(t)
        if(s==t):
            return True
        else:
            return False
    def delete(self,S):
        res=[]
        for i in S:
            if(i=='#'):
                if(res):
                    res.pop()
            else:
                res.append(i)
        l = ''.join(res)
        return l  




res = Solution()
s="#c"
t="ad##c"
ans = res.backspaceCompare(s,t)
print(ans)