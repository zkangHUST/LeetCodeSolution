class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = sum(nums)
        b = (0 + n) * (n + 1) // 2
        return b - a