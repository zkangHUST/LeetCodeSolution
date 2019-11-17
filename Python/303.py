class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = [[0 for i in range(len(nums))] for j in range(len(nums))]

        

    def sumRange(self, i: int, j: int) -> int:
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        for i in range(len(self.nums)):
            for j in range(i, len(self.nums)):
                if i == j:
                    self.dp[i][j] = self.nums[i]
                else:
                    self.dp[i][j] = self.dp[i][j - 1] + self.nums[j]
        return self.dp[i][j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)