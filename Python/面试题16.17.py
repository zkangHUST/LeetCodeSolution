class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -2147483648
        dp = [0 for i in range(len(nums))]
        ans = nums[0]
        for i in range(len(nums)):
            dp[i] = nums[i]
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1] + nums[i])
            ans = max(ans, dp[i])
        return ans