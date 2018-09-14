class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        val = left
        while(val <= right):
            if (self.check(val)):
                l.append(val)
            val += 1
        return l
    def check(self,value):
        v = str(value)
        if (v.count('0') != 0):
            return False
        for key in v:
            if value%(int(key)) != 0:
                return False
        return True
res = Solution()
ans = res.selfDividingNumbers(1,22)
print(ans)
