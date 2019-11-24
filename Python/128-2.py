class Solution:
    def longestConsecutive(self, nums):
        cnt = {i for i in nums}
        m = 0
        for i in nums:
            if i - 1 not in cnt:
                l = 0
                while i in cnt:
                    l += 1
                    i += 1
                m = max(m, l)
        return m 

p = Solution()
nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
print(p.longestConsecutive(nums))