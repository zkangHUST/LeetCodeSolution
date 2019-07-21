class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        minlen = len(nums) + 1
        i = j = 0
        m = 0
        while j < len(nums):  
            m += nums[j]
            while m >= s:
                if j - i + 1 < minlen:
                    minlen = j - i + 1
                m -= nums[i]
                i += 1
            else:
                j += 1
        if minlen == len(nums) + 1:
            return 0
        return minlen