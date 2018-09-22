class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        length = len(nums)
        nums.sort()
        i = 0
        while(i < length):
            j = i + 1
            k = length - 1
            target = 0 - nums[i]
            while(j < k):
                tmp  = nums[j] + nums[k]
                if (tmp > target):
                    k -= 1
                elif (tmp < target):
                    j += 1
                else:
                    ans.clear()
                    ans.append(nums[i])
                    ans.append(nums[j])
                    ans.append(nums[k])
                    res.append(ans[:])
                    while(j < k and nums[j] == ans[1]):
                        j += 1
                    while(j < k and nums[k] == ans[2]):
                        k -= 1
            while (i + 1 < length and  nums[i + 1] == nums[i]):
                i += 1
            i += 1              
        return res

res = Solution()
nums=  [-1, 0, 1, 2, -1, -4]
ans = res.threeSum(nums)
print(ans)