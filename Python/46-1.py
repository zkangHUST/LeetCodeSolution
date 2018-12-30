class Solution:
    def permute(self, nums):
        self.result = []
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = []
        self.trace(nums, s, 0)
        return self.result
    def trace(self, nums, s, n):
        if (n == len(nums)):
            self.result.append(s)
            return
        for i in range(len(nums)):
            if (nums[i] not in s):
                self.trace(nums, s+[nums[i]], n+1)
res = Solution()
nums = [1,2,3]
# print(nums)
l = res.permute(nums)
print(l)
