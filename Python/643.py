class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = m = sum(nums[:k])
        i = 0
        j = k
        while (j < len(nums)):
            m -= nums[i]
            m += nums[j]
            i += 1
            j += 1    
            if (m > n):
                n = m
        return n/k

nums = [1,12,-5,-6,50,3]
k = 4
res = Solution()
ans = res.findMaxAverage(nums, k)
print(ans)