import math
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        m, n = -math.inf, -math.inf 
        idx = 0
        for i in range(len(nums)):
            if nums[i] > m:
                idx, n, m = i,  m, nums[i]
            elif nums[i] > n:
                n = nums[i]
        if m >= 2 * n:
            return idx
        return -1