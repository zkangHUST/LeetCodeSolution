class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        path = []
        nums = sorted(candidates)
        self.get(nums, target, 0, path)
        return self.ans
    def get(self, nums, target, start, path):
        if target < 0:
            return 
        if target == 0:
            if path not in self.ans:
                self.ans.append(path)
            return 
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.get(nums, target - nums[i], i + 1, path[:])
            path.pop()