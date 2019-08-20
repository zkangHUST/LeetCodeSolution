# 回溯法求子集
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        s = []
        l = len(nums)
        self.backtrace(nums, 0, l, s, ans) 
        return ans
    def backtrace(self, nums, i, cnt, s, ans):
        if i >= cnt:
            ans.append(s)
            return 
        s.append(nums[i])
        self.backtrace(nums, i + 1, cnt, s[:], ans)
        s.pop()
        self.backtrace(nums, i + 1, cnt, s[:], ans)
        