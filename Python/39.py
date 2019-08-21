class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        path = []
        self.get(candidates, target, path, 0)
        return self.res
    def get(self, nums, target, path, start):
        if target < 0:
            return 
        elif target == 0:
            if path not in self.res:
                self.res.append(path)
            return 
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.get(nums, target - nums[i], path[:], i)
            path.pop()