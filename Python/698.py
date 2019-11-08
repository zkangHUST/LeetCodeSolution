class Solution:
    def canPartitionKSubsets(self, nums, k):    
        if sum(nums) % k != 0:
            return False
        target = sum(nums) / k
        path = [0 for i in range(0, k)]
        self.ans = False
        self.dfs(nums, path, 0, len(nums), k, target)
        return self.ans
    def dfs(self, nums, path, cnt, length, k, target):
        if self.ans:
            return 
        if cnt  == length:
            self.ans = True
            return
        if cnt + 1 < k:
            m = cnt + 1
        else:
            m = k
        for i in range(0, m):
            if path[i] + nums[cnt] > target:
                continue
            path[i] += nums[cnt]
            self.dfs(nums, path, cnt + 1, length, k, target)
            path[i] -= nums[cnt]

nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
k = 5
p = Solution()
print(p.canPartitionKSubsets(nums, k))