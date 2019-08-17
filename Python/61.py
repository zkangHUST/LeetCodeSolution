# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        if k <= 0:
            return head
        p = head
        len = 1
        while p.next:
            len += 1
            p = p.next
        p.next = head 
        tmp = p
        p = head
        k = len - k % len
        while k > 0:
            tmp = p
            p = p.next
            k -= 1
            
        tmp.next = None
        return p
            