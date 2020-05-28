class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        dp = [1 for i in range(len(nums))]
        last = [-1 for i in range(len(nums))]
        nums = sorted(nums)
        l = 0
        end = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    last[i] = j
                if dp[i] > l:
                    l = dp[i]
                    end = i
        i = end
        ans = []
        while i != -1:
            ans.append(nums[i])
            i = last[i]
        return ans