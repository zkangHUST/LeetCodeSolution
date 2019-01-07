class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0
        if (len(typed) < len(name)):
            return False
        while (i < len(name) and j < len(typed)):
            if (name[i] == typed[j]):
                i += 1
                j += 1
            elif(j > 0 and typed[j] == typed[j -1]):
                j+=1
            else:
                return False
        if (i < len(name)):
            return False
        while(j < len(typed)):
            if (typed[j] != name[-1]):
                return False
            j += 1
        return True
       

p = "pyplrz"
q = "ppyypllr"
res = Solution()
l = res.isLongPressedName(p,q)
print(l)
