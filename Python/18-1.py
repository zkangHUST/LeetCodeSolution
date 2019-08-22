class Solution:
    def fourSum(self, nums, target):
        self.ans = []
        nums = sorted(nums)
        path = []
        self.get(nums, target, 4, path)
        return self.ans
    def get(self, nums, target, n, path):
        if n == 2:
            self.twosum(nums, target, path)
            return 
        if len(nums) < n:
            return 
        for i in range(len(nums)):    
            path.append(nums[i])
            self.get(nums[i + 1:], target - nums[i], n - 1, path[:])
            path.pop()
    def twosum(self, nums, target, path):
        i, j = 0, len(nums)
        while i < j:
            tmp = nums[i] + nums[j]
            if tmp == target:
                p = path[:]
                p.append(nums[i])
                p.append(nums[j])
                i += 1
                j -= 1
                if p not in self.ans:
                    self.ans.append(p)
            elif tmp < target:
                i += 1
            else:
                j -= 1


nums = [-3,-2,-1,0,0,1,2,3]
p = Solution()
print(p.fourSum(nums, 0))
