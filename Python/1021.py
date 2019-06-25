class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt = 0
        res = ""
        i = 0
        j = 0
        while j < len(S):
            if (S[j] == '('):
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0 :
                res += S[i + 1:j]
                j += 1
                i = j
            else:
                j += 1
        return res
            