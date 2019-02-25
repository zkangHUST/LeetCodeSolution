class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        i = 0
        tmp = []
        res = []
        while(i < numRows):
            tmp = self.getN(i,tmp)
            res.append(tmp[:])
            i += 1
        return res
    def getN(self, n, l):
        if (n == 0):
            return [1]
        elif (n == 1):
            return [1,1]
        else:
            tmp = []
            for i in range(0, len(l) - 1):
                tmp.append(l[i] + l[i + 1])
            tmp = [1] + tmp + [1]
        return tmp 
res = Solution()
l = res.generate(4)
print(l)