class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = []
        for v in s:
            if v == '[' or v == '(' or v == '{':
                tmp.append(v)
            elif tmp == []:
                return False
            elif v == ']':
                if tmp[-1] != '[':
                    return False
                tmp.pop()
            elif v == ')':
                if tmp[-1] != '(':
                    return False
                tmp.pop()
            elif v == '}':
                if tmp[-1] != '{':
                    return False
                tmp.pop()
        if tmp != [] :
            return False
        return True
s = "{[]"
res = Solution()
print(res.isValid(s))