class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1  
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            # in the left side
            if nums[mid] >= nums[0]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # in the right side 
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

