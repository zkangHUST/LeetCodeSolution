# 核心想法是从先找一个范围[i, j],这个范围内的乘积小于k,
# 那么遍历i+1的时候，[i + 1, j]这个范围内的乘积也是小于k的，直接可以得到个数，然后从j+1开始就可以了

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        dp = [[0] * len(nums)] * len(nums)
        cnt = 0
        length = len(nums)
        lastj = 0
        for i in range(length):
            if (lastj < i):
                lastj = i
                dp[i][lastj] = nums[i]
            elif (lastj > i):
                cnt += (lastj - i)
                dp[i][lastj] = dp[i - 1][lastj] / nums[i - 1]
            else:
                dp[i][lastj] = nums[i]
            if (dp[i][lastj] < k):
                cnt += 1
            for j in range(lastj + 1 , length):
                dp[i][j] = dp[i][j - 1] * nums[j]
                if dp[i][j] < k:
                    cnt += 1
                    lastj = j
                else:
                    break
        return cnt