class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtracking(S=[],i=1,l=k):
            if l==0:
                res.append(S)
                return
            for i in range(i,n+1):
                backtracking(S+[i],i+1,l-1)
        backtracking()
        return res
res = Solution()
l = res.combine(4,2)
print(l)
