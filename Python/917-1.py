class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        j = len(S) - 1
        tmp = list(S)
        while (i < j):
            if tmp[i].isalpha():
                if tmp[j].isalpha():
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    i += 1
                j -= 1
            else:
                i += 1
        return "".join(tmp)

if __name__ == '__main__':
    res = Solution()
    S =  "Test1ng-Leet=code-Q!"
    ans = res.reverseOnlyLetters(S)
    print(ans)