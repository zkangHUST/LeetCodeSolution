from math import sqrt
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = int(sqrt(2*n)-1)
        i=0 if(i<0) else i
        while(1):
            if(i*(i+1)<2*n):
                i+=1
            elif(i*(i+1)==2*n):
                break
            else:
                i-=1
                break
        return i