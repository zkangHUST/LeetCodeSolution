class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        j = len(S) - 1
        res = ""
        while(j >= 0 and S[j].isalpha() == False):
            j -= 1
        while(i < len(S) and  j >= 0):
            if (S[i].isalpha()):
               res += S[j]
               j-=1
            else :
                res += S[i]
            while(j >= 0 and not S[j].isalpha()):
                j -= 1    
            i+=1
        res += S[i:]
        return res
res = Solution()
s = "Test1ng-Leet=code-Q!"

d = res.reverseOnlyLetters(s)
print(d)

    
        