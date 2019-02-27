#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (73.33%)
# Total Accepted:    30.9K
# Total Submissions: 42.3K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# 
# 
# 
# Example 2:
# 
# 
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
# 
# 
# 
# 
#
class Solution:
    def sortedSquares(self, A):
        if len(A) == 0 :
            return []
        i = 0
        while True:
            if A[i] >= 0:
                break
            key = -A[i]
            del A[i]
            if len(A) == 0:
                A.append(key)
            else:
                for i in range(len(A)):
                    if key <= A[i]:
                        A.insert(i, key)
                        break
                if i == len(A) - 1:
                    A.append(key)
            i = 0
        ans = [val ** 2 for val in A]
        return ans

res = Solution()
s = [-9,0, 1]
ans = res.sortedSquares(s)        
print(ans)




            

