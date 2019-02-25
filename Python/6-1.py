class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        l = [''] * numRows
        index = 0
        flag = 0
        for v in s:
            l[index] += v
            if (index == numRows -1):
                flag = 1
            elif (index == 0): 
                flag = 0
            if(flag == 0):
                index += 1
            else:
                index -= 1
        return ''.join(l)

