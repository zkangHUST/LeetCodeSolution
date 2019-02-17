#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (41.74%)
# Total Accepted:    182K
# Total Submissions: 435.8K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex == 0:
            return [1]
        elif(rowIndex == 1):
            return [1, 1]
        tmp = [1, 1]
        for i in range(rowIndex - 1):
            tmp = self.getNextRow(tmp)
        return tmp
    def getNextRow(self, s):
        tmp = [1]
        for i in range(len(s) - 1):
            tmp.append(s[i] + s[i + 1])
        tmp.append(1)
        return tmp
if __name__ == "__main__":
    res = Solution()
    ans = res.getRow(3)
    print(ans)       
        
