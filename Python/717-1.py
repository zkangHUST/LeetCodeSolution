class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        if n == 1:
            return True
        elif n == 2:
            if bits[0] == 1:
                return False
            else:
                return True
        i = 0
        while i < n-1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        if i == n-1:
            return True
        else:
            return False

res=Solution()
l = [0 ,0]
ans = res.isOneBitCharacter(l)
print(ans)
