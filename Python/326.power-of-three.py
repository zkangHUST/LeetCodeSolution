#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (41.34%)
# Total Accepted:    167.9K
# Total Submissions: 406.2K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
# 
# Example 1:
# 
# 
# Input: 27
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: false
# 
# Example 3:
# 
# 
# Input: 9
# Output: true
# 
# Example 4:
# 
# 
# Input: 45
# Output: false
# 
# Follow up:
# Could you do it without using any loop / recursion?
#
class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if (n % 2 == 0):
            return False
        res = 1
        while True:
            if (res == n):
                return True
            elif(res > n):
                return False
            res *= 3        
