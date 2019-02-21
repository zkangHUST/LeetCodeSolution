# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        p = head
        while(p):
            if (p and p.next):
                # tmp = p.val
                # p.val = p.next.val
                # p.next.val = tmp
                p.val, p.next.val = p.next.val,p.val
            if (p.next):
                p = p.next.next  
            else:
                break  
        return head
