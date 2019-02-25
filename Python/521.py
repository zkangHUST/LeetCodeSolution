class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        lena = len(a)
        lenb = len(b)
        if (lena > lenb):
            return lena
        elif(lena < lenb):
            return lenb
        if a == b :
            return -1
        return lena
        