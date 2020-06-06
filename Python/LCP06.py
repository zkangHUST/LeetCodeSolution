class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        ans = 0
        for n in coins:
            ans += (n + 1) // 2
        return ans