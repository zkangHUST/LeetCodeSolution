class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = [0 for i in range(len(nums) + 1)]
        ans = []
        for val in nums:
            if visited[val] == 0:
                visited[val] = 1
            else:
                 ans.append(val)
        for i in range(1, len(visited)):
            if visited[i] == 0:
                ans.append(i)
                break
        return ans