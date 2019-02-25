#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#
# https://leetcode.com/problems/powerful-integers/description/
#
# algorithms
# Easy (39.38%)
# Total Accepted:    7.3K
# Total Submissions: 18.5K
# Testcase Example:  '2\n3\n10'
#
# Given two non-negative integers x and y, an integer is powerful if it is
# equal to x^i + y^j for some integers i >= 0 and j >= 0.
# 
# Return a list of all powerful integers that have value less than or equal to
# bound.
# 
# You may return the answer in any order.  In your answer, each value should
# occur at most once.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation: 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 
# 
# 
# Example 2:
# 
# 
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6
# 
# 
#
class Solution:
    def powerfulIntegers(self, x: 'int', y: 'int', bound: 'int') -> 'List[int]':
        i = 0
        j = 0
        l = set()
        while True:
            while True:
                n = x ** i + y ** j
                if (n <= bound):
                    l.add(n)
                    if (y == 1):
                        break
                    j += 1
                else:
                    break
            i += 1
            j = 0
            if (x == 1):
                break
            if (x ** i + 1 > bound):
                break
        return list(l)
res = Solution()
ans = res.powerfulIntegers(1, 1, 100)
print(ans)
