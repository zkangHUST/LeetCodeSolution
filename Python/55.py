class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(len(dp)):
            if dp[-1] == 1:
                return True
            if dp[i] != 1:
                return False
            for j in range(nums[i], 0, -1):
                if i + j < len(dp):
                    if dp[i + j] == 1:
                        break
                    else:
                        dp[i + j] = 1
                        
        return dp[-1]