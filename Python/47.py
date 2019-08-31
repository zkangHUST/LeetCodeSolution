class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        visited = [0 for i in range(len(nums))]
        path = []
        self.dfs(nums, 1, visited, path)
        return self.ans
    def dfs(self, nums, cnt, visited, path):
        if cnt > len(nums):
            if path not in self.ans:
                self.ans.append(path)
            return
        for i in range(len(nums)):
            if visited[i] == 1:
                continue
            path.append(nums[i])
            visited[i] = 1
            self.dfs(nums, cnt + 1, visited, path[:])
            path.pop()
            visited[i] = 0