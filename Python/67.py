class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        #bin转换后的格式为0b100
        return bin(a+b)[2:]        
res = Solution()
ans = res.addBinary("1010",'1011')
print(ans)
