class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = nums[0]
        minites = nums[:]
        for i in range(1, len(minites)):
            for j in range(i - 1):
                minites[i] = max(minites[i], minites[j] + nums[i])
            ans = max(ans, minites[i])
        return ans