class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = {}
        for i in range(ord('a'), ord('z') + 1):
            nums[chr(i)] = 0
        for v in s:
            nums[v] += 1
        sorted(nums.items(),key=lambda x: x[1], reverse=True)
        s= ''
        for x in nums:
            s += x.key()
        print(nums)
        return s
s = "abcabcccdddddddd"
res = Solution()
l = res.frequencySort(s)
print(l)
# num =dict()
# s="abca"
# for v in s:
#     num[v] = 1
# print(num)