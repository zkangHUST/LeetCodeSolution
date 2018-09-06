class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res= bin(n)[2:]
        index = res[0];
        for key in res[1:]:
            if key !=index:
                index = key
                continue
            else:
                return False
        return True
        