class Solution:
    def fourSum(self, nums, target):
        self.ans = []
        nums = sorted(nums)
        path = []
        self.get(nums, 0, 0, path, target)
        return self.ans
    def get(self, nums, cnt, begin, path, target):
        if begin > len(nums):
            return 
        if cnt == 4:
            if target == 0:
                if path not in self.ans:
                    self.ans.append(path)
            return 
        for i in range(begin, len(nums)):
            path.append(nums[i])
            self.get(nums, cnt + 1, i + 1, path[:], target - nums[i])
            path.pop()



nums = [-3,-2,-1,0,0,1,2,3]
p = Solution()
print(p.fourSum(nums, 0))
