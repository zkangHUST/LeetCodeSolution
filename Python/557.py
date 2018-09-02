class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s.split()
        ans=""
        for temp in res:
            ans= ans +' '+temp[::-1]
        ans = ans.lstrip()
        return ans
           
    

res = Solution()
s="Let's take LeetCode contest"
s= res.reverseWords(s)
print(s)