class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]
        for n in nums:
            if n == 0:
                cnt[0] += 1
            elif n == 1:
                cnt[1] += 1
            else:
                cnt[2] += 1
        for i in range(len(nums)):
            if cnt[0] > 0:
                nums[i] = 0
                cnt[0] -= 1
            elif cnt[1] > 0:
                nums[i] = 1
                cnt[1] -= 1
            else:
                nums[i] = 2
                