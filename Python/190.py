class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        res=bin(n)[2:]
        res = '0' * (32 - len(res)) + res
        res=res[::-1]
        return int(res,2)

res = Solution()
ans = res.reverseBits(43261596)
print(ans)   