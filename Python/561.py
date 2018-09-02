class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        nums = nums[::2]
        print(nums)
        return sum(nums)
res = Solution()
nums=[1,3,2,4,5,6, 7,8,9,10]
print (res.arrayPairSum(nums))