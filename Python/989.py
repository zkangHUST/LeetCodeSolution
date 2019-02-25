class Solution:
    def addToArrayForm(self, A, K):
        ans = 0
        for val in A:
            ans = ans * 10 + val 
        ans += K
        x = [int(val) for val in list(str(ans))]
        return x
res = Solution()
ans = res.addToArrayForm([1,2,3], 4)
print(ans)