class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = set()
        for val in nums:
            if val not in l:
                l.add(val)
            else:
                l.remove(val)
        res = list(l)
        return res   
res = Solution()
nums =  [1,2,1,3,2,5]
ans = res.singleNumber(nums) 
print(ans)