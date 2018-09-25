class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while(i + 1 < len(nums)):
            if (nums[i] != nums[i+1]):
                return nums[i]
            else:
                i += 2
        return nums[-1]
nums =  [1,1,2,3,3,4,4,8,8]
res = Solution()
ans = res.singleNonDuplicate(nums)
print(ans)
