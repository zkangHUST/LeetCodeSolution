class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        size = len(s)
        ans = ""
        num = ""
        tmpstr = ""
        stack = []
        i = 0 
        while i < size:
            while i < size and s[i] >= '0' and s[i] <= '9':
                num += s[i]
                i += 1
            if num:
                stack.append(num)
                num = ""
                continue
            while i < size and  s[i].isalpha() :
                tmpstr += s[i]
                i += 1
            if tmpstr:
                stack.append(tmpstr)
                tmpstr = ""
                continue
            if s[i] == '[':
                stack.append(s[i])
            elif s[i] == ']':
                cnt = 0
                ans = stack.pop(-1)
                while stack:
                    tmp = stack.pop(-1)
                    if tmp.isdigit():
                        ans = ans * int(tmp)
                    elif tmp.isalpha(): 
                        ans = tmp + ans
                    elif tmp == '[':
                        cnt += 1
                        if cnt == 2:
                            break 
                stack.append(ans)
            i += 1
        ans = stack.pop(-1)
        while stack:
            tmp = stack.pop(-1)
            if tmp.isdigit():
                ans = ans * int(tmp)
            else:
                ans = tmp + ans
        return ans

s = Solution()
ss = "3[a]2[b4[F]c]"
ans = s.decodeString(ss)
print(ans)