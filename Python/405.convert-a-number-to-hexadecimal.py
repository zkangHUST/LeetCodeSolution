#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (41.63%)
# Total Accepted:    43.5K
# Total Submissions: 104.5K
# Testcase Example:  '26'
#
# 
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
# 
# 
# Note:
# 
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
# 
# 
# 
# Example 1:
# 
# Input:
# 26
# 
# Output:
# "1a"
# 
# 
# 
# Example 2:
# 
# Input:
# -1
# 
# Output:
# "ffffffff"
# 
# 
#
class Solution:
    def toHex(self, num: 'int') -> 'str':
        if num == 0:
            return '0'
        key = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f']
        
        if (num < 0):
            num += 4294967296
        res = []
        while(num):
            tmp = num % 16
            res.insert(0, key[tmp])
            num = num // 16
        l = ''.join(res)
        return l
res = Solution()
ans = res.toHex(42949672960)
print(ans)  
