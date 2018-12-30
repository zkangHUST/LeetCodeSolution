class Solution:
    def permute(self, nums):
        self.result = []
        self.tmp = []
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.trace(nums, 0)
        return self.result
    def trace(self, nums, n):
        if (n == len(nums)):
            self.result.append(self.tmp[:])
            return
        for i in range(len(nums)):
            if (nums[i] not in self.tmp):
                self.tmp.append(nums[i])
                self.trace(nums,n+1)
                self.tmp.remove(nums[i])
res = Solution()
nums = [1,2,3,4]
l = res.permute(nums)
print(l)
