class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #注意考虑长度为1的情况，不处理下面的代码会出现下标越界的情况
        if(len(nums)==1):
            return 0
        for i in range(len(nums)):
            if(i==0):
                if(nums[i]>nums[i+1]):
                    break
            elif(i == len(nums)-1):
                if(nums[i]>nums[i-1]):
                    break             
            else:
                if(nums[i]>nums[i+1] and nums[i]>nums[i-1]):
                    break
        return i

res = Solution()
l = [101]
ans = res.findPeakElement(l)
print(ans)
