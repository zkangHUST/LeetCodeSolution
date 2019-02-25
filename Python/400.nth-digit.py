#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.04%)
# Total Accepted:    44K
# Total Submissions: 146.4K
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution:
    def findNthDigit(self, n: 'int') -> 'int':
        tmp = 0
        i = 1
        num = 0
        while(True):
            if (tmp + 9 * i * 10**(i-1) >= n):
                break
            else:
                tmp += (9 * i * 10**(i -1))
                i += 1
        # tmp + num * i >= n
        num = (n - tmp) / i
        # num = num > int(num)?int(num) + 1:int 
        if (num > int(num)):
            num = int(num) + 1
        else:
            num = int(num)
        if(num > 0):
            tmp += (num - 1) * i
        k = 10 ** (i - 1) + num - 1
        return int(str(k)[n - tmp - 1])
# res = Solution()
# for i in range(189, 200):
#     ans = res.findNthDigit(i)
#     print(ans)
