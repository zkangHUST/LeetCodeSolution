class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num = [1, 2, 3, 1, 2, 3]
        k = 2
        cnt = {}
        for i in range(len(nums)):
            if nums[i] in cnt and i - cnt[nums[i]] <= k:
                return True
            cnt[nums[i]] = i

        return False