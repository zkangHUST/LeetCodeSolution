#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (39.32%)
# Total Accepted:    254.8K
# Total Submissions: 648.1K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        tmp = "1"
        for i in range(n - 1):
            tmp = self.say(tmp)
        return tmp
    def say(self, s):
        res = ""
        count = 0
        for i in range(len(s) - 1):
            count += 1
            if s[i] != s[i + 1]:
                res += (str(count) + s[i]) 
                count = 0
        res += (str(count + 1) + s[-1])
        return res

res = Solution()
ans = res.countAndSay(6)
print(ans)
