class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in range(pow(2,n)):
            #格雷码生成规则
            res.append(i ^(i>>1))
        return res

res = Solution()
print(res.grayCode(0))
        
        