from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        for c in combinations([i for i in range(1,n+1)], k):
            res.append(list(c))
        return res

res = Solution()
l = res.combine(4,2)
print(l)