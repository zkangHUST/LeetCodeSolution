class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cnt = {}
        for i in range(len(nums)):
            if nums[i] in cnt and i - cnt[nums[i]] <= k:
                return True
            cnt[nums[i]] = i

        return False