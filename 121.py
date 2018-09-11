class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) == 0):
            return 0
        m = prices[0]
        n = 0
        for val  in prices:
            if (val < m):
                m = val
            profit = val - m
            if(profit > n):
                n = profit
        return n
        