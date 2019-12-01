class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxlen = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
                if cnt > maxlen:
                    maxlen = cnt
            else:
                cnt = 1
        return maxlen