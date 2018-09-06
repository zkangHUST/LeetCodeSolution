class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

res = Solution()
ans = res.hammingWeight(5)
print(ans)