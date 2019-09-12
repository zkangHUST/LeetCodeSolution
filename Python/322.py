class Solution:
    def coinChange(self, coins, amount):
        dp = [-1 for i in range(amount + 1)]
        for i in range(amount + 1):
            if i in coins:
                dp[i] = 1
                continue    
            for j in coins:
                if i - j < 0:
                    continue
                if dp[i - j] == -1:
                    continue
                if dp[i] == -1:
                    dp[i] = dp[i - j] + 1
                else:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[amount]        

coins = [1]
p = Solution() 
ans = p.coinChange(coins, 0)
