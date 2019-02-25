class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        length = len(nums)
        for i in range(length - 1):
            if (nums[i] > nums[i + 1]):
                cnt += 1
        if (cnt > 1) :
            return False
        return True

num = []
res = Solution()
print(res.checkPossibility(num))
