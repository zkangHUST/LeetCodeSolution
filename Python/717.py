class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if(len(bits)==1):
            return True
        elif(len(bits)==2 and bits[0]==1):
            return False
        elif(bits[0]==0):
            res = self.isOneBitCharacter(bits[1:])
            return res
        elif (bits[0]==1):
            return self.isOneBitCharacter(bits[2:])


res=Solution()
l = [1,0,0]
ans = res.isOneBitCharacter(l)
print(ans)
