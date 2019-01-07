class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        i = 0
        res = ""
        S = S.split()
        while(i < len(S)):
            if S[i][0] in vowel:
                l = S[i] + "ma" + 'a'*(i + 1)
            else:
                l = S[i][1:] + S[i][0] + 'ma' + 'a'*(i+1)
            if i == len(S) - 1:
                res += l
            else:
                res += (l + ' ')
            i += 1
        return res

res = Solution()
S = "I speak Goat Latin"
l = res.toGoatLatin(S)
print(l)