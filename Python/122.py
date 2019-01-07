class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        if not prices:
            return 0
        valley = prices[0]
        peak = prices[0]
        result = 0
        length = len(prices)
        while(i < length - 1):
            while(i < length - 1 and prices[i] >= prices[i + 1]):
                i += 1
            valley = prices[i]
            while(i < length - 1 and prices[i] <= prices[i + 1]):
                i += 1
            peak = prices[i]
            result += peak - valley
        return result
res = Solution()
prices = [3,3]
l = res.maxProfit(prices)
print(l)