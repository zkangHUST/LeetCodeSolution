# 回溯法求子集
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        s = []
        l = len(nums)
        self.backtrace(nums, 0, l, s, ans) 
        return ans
    def backtrace(self, nums, i, cnt, s, ans):
        if i >= cnt:
            tmp = sorted(s) 
            if tmp not in ans:
                ans.append(tmp[:])
            return
        s.append(nums[i])
        self.backtrace(nums, i + 1, cnt, s[:], ans)
        s.pop()
        self.backtrace(nums, i + 1, cnt, s[:], ans)
        