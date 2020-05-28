class Solution:
    def decodeString(self, s: str) -> str:
        i, stack = 0, []
        while i < len(s):
            if s[i] == '[' or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
                stack.append(s[i])
                i += 1
            elif s[i] >= '0' and s[i] <= '9':
                num = 0
                while i < len(s) and s[i] >= '0' and s[i] <= '9':
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                stack.append(num)
            else:
                tmp = ""
                ch = stack.pop()
                while ch != '[':
                    tmp = ch + tmp
                    ch = stack.pop()
                ch = stack.pop()
                tmp = tmp * ch
                stack.append(tmp)
                i += 1
        return "".join(stack)

a = Solution()
# b = "3[a2[c]]"
# ans = a.decodeString(b)
for b in ["3[a]2[b4[F]c]"]:
    ans = a.decodeString(b)
    print(ans)


                

