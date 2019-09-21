class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxdp = [nums[0]] * len(nums)
        mindp = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            maxdp[i] = max(mindp[i-1]*nums[i], maxdp[i-1]*nums[i], nums[i])
            mindp[i] = min(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])

        return max(maxdp)

p = Solution()
nums = [2,3,-2,4]
ans = p.maxProduct(nums)
