class Solution:
    def longestConsecutive(self, nums):
        cnt = {}
        for i in nums:
            if i in cnt:
                continue
            if i - 1 in cnt:
                l = cnt[i - 1]
            else:
                l = 0
            if i + 1 in cnt:
                r = cnt[i + 1]
            else:
                r = 0
            cnt[i] = l + r + 1
            cnt[i - l] = l + r + 1
            cnt[i + r] = l + r + 1
        m = 0
        for i in cnt:
            m = max(m, cnt[i])
        return m


p = Solution()
nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
print(p.longestConsecutive(nums))