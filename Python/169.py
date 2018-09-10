class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        l =set()
        for val in nums:
            if val not in l:
                cnt= nums.count(val)
                if cnt > length//2:
                    return val
                else:
                    l.add(val)
