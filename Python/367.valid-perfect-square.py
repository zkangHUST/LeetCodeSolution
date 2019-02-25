#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.32%)
# Total Accepted:    98.9K
# Total Submissions: 251.4K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#
class Solution:
    def isPerfectSquare(self, num: 'int') -> 'bool':
        left = 1
        right = num
        mid = left + (right - left) // 2
        while True:
            if (mid * mid < num and (mid + 1) * (mid + 1) > num):
                return False
            elif (mid * mid < num):
                left = mid + 1
            elif (mid * mid > num):
                right = mid - 1
            else:
                return True
            mid = left + (right - left) // 2 
# res = Solution()
# for i in range(101):
#     ans = res.isPerfectSquare(i)
#     print("%d = %s"%(i, ans))      
