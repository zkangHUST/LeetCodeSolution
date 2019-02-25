class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        if (length < 4):
            return []
        index = [1,2,3]
        res = []
        for i in range(2,-1,-1):
            while (i == 2 and index[2] <= length):
                if (index[2] == length): 
                    index[2]-=1
                    break
                key = self.getnum(s,index)
                if (key):
                    res.append(key) 
                index[i] += 1
            while (i < 2 and index[i] <= index[i+1]):
                if (index[i] == index[i+1]):
                    index[i] -= 1
                    break
                key = self.getnum(s,index)
                if(key and key not in res):
                    res.append(key)
                index[i]+=1
        return res
    def getnum(self,s,index):
        key = []
        key.append(int(s[0:index[0]]))
        key.append(int(s[index[0]:index[1]]))
        key.append(int(s[index[1]:index[2]]))
        key.append(int(s[index[2]:]))
        for i in range(4): 
            if (key[i] > 255):
                return []
        return key
res = Solution()
v = "25525511135"
l = res.restoreIpAddresses(v)
print(l)