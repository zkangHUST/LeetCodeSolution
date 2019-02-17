#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (44.81%)
# Total Accepted:    207.9K
# Total Submissions: 463.8K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        result = []
        if (root == None):
            return []
        else:
            tmp = str(root.val)
            if (root.left == None and root.right == None):
                result.append(tmp)
            if root.left:
                self.treeTravel(root.left, tmp[:], result)
            if root.right:
                self.treeTravel(root.right, tmp[:], result)
        return result
    def treeTravel(self, root, p, result):
        if (not root):
            return
        if (root and root.left == None and root.right == None):
            p += ("->" + str(root.val))
            result.append(p[:])
        else:
            p += ("->" + str(root.val))
            if (root.left):
                self.treeTravel(root.left, p[:], result)
            if (root.right):
                self.treeTravel(root.right, p[:], result)
            return 

