class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        print(p)
        ans = []
        for c in p:
            if not c :
                continue
            if c == "..":
                if ans:
                    ans.pop(-1)
            elif c == "/" or c == ".":
                continue
            else:
                ans.append(c)
        ret = "/"
        for i in range(len(ans)):
            ret += ans[i]
            if i < len(ans) - 1:
                ret += "/"
        return ret


p = Solution()
r = "/../../..//.."
s = p.simplifyPath(r)
print(s)
