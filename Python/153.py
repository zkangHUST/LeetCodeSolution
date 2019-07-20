class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[mid]
        


nums = [3,2, 1]

res = Solution()
ans = res.findMin(nums)
print(ans)
