class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        l = set()
        for i in range(k+1):
            if nums[i] not in l:
                l.add(nums[i])
            else:
                return true
        while(i < length):
            l.remove(l[0])
            if nums[i] not in l:
                l.add(nums[i])
            else:
                return true
            i++
        return false
