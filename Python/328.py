# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        evenhead = head.next
        p = head
        q = head.next
        while p and q:
            p.next  = q.next
            tmp = p
            p = p.next
            if p:
                q.next = p.next
            else:
                q.next = None
            q = q.next
        if p:
            p.next = evenhead
        else:
            tmp.next = evenhead
        return head