class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        i = 0
        j = 1
        l = []
        while(j < length):
            if(self.check(S[i:j], S[j:]) == True):
                j+=1
            else:
                l.append(j-i)
                i = j
                j += 1
        if (j-i != 0):
            l.append(j - i)
        return l
    def check(self, l1, l2):
        for v in l1:
            if v in l2:
                return True
        return False


res = Solution()
S= "ababcbacadefegdehijhklij"
ans = res.partitionLabels(S)
print(ans)