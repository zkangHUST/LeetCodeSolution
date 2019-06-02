class Solution:
    def queryString(self, S: str, N: int):
        for i in range(1, N + 1):
            tmp = bin(i)[2:]
            if S.count(tmp) == 0:
                return  False
        return True

res = Solution()
ans = res.queryString("0110",3)
print(ans)
