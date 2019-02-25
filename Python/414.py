class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c =min(nums)
        for key in nums:
            if key > c:
                a = b
                b = c
                c = key
            elif key > b and key != c:
                a = b
                b = key
            elif key > a and key != b and key != c:
                a = key
        if (a < b < c):
            return a
        else: 
            return c
# res = Solution()
# nums = [1,2,2,5,3,5]
# print(res.thirdMax(nums))