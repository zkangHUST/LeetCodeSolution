#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (63.13%)
# Total Accepted:    43.9K
# Total Submissions: 69.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a non-empty, singly linked list with head node head, return a middle
# node of linked list.
# 
# If there are two middle nodes, return the second middle node.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is
# [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
# = NULL.
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second
# one.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given list will be between 1 and 100.
# 
# 
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        if (head == None):
            return 
        fast = head
        slow = head
        while(fast):
            if (fast.next):
                fast = fast.next
            slow = slow.next
        return slow
