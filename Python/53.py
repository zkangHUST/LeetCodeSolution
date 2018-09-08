class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        large = nums[0]
        for val in nums:
            res += val
            if (res > large):
                large = res
            if (res < 0):
                res = 0
        return large

res = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = res.maxSubArray(nums)
print(ans)
