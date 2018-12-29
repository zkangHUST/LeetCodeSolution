class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (not nums): 
            return [-1, -1]
        i = 0
        j = len(nums) - 1
        while(i < j):
            while(i < j and nums[i] != target):
                i += 1
            while(i < j and nums[j] != target):
                j -= 1
            break
        if (nums[i] != target):
            return [-1,-1]
        else:
            return [i,j]

if __name__ == '__main__':
    res = Solution()
    # nums = [5,7,7,8,8,10]
    nums = []
    target = 0
    ret = res.searchRange(nums, target)
    print(ret)