# 双指针法

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        tmp = 1
        cnt = 0
        left = right = 0
        size = len(nums)
        while left < size and right < size:
            tmp *= nums[right]
            while (tmp >= k and left <= right):
                tmp /= nums[left]
                left += 1
            if tmp < k and left <= right:
                cnt += right - left + 1
            right += 1
        return cnt