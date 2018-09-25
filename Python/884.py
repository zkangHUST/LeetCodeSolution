class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        res = []
        l1 = A.split(' ') + B.split(' ')
        for key in l1:
            if l1.count(key) == 1:
                res.append(key)    
        return res
res = Solution()
A = "this apple is sweet"
B = "this apple is sour"
ans = res.uncommonFromSentences(A, B)
print(ans)