class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.ans = False
        nums = []
        self.dfs(0, num, nums)
        return self.ans
    
    def dfs(self, s, str, nums):
        if s >= len(str):
            if len(nums) < 3:
                self.ans = False
                return
            self.ans = True
            return 

        if str[s] == '0':
            if len(nums) < 2:
                res = nums[:]
                res.append(0)
                self.dfs(s + 1, str, res)
            elif nums[-1] + nums[-2] == 0:
                    res = nums[:]
                    res.append(0)
                    self.dfs(s + 1, str, res)
            return

        for i in range(s + 1, len(str) + 1):
            if self.ans:
                return
            tmp = int(str[s:i])
            if len(nums)  < 2:
                res = nums[:]
                res.append(tmp)
                self.dfs(i, str, res)
            elif tmp == nums[-1] + nums[-2]:
                res = nums[:]
                res.append(tmp)
                self.dfs(i, str, res)



s = Solution()
num = "0235813"
ans = s.isAdditiveNumber(num)
print(ans)