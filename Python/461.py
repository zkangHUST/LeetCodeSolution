class Solution():
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")

ans = Solution()
x= ans.hammingDistance(1, 4)
print(x)
