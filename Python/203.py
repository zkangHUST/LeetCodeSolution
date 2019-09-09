# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = head
        while p and p.val == val:
            p = p.next
        q = p
        while q and q.next:
            if q.next.val == val:
                q.next = q.next.next
            else:
                q = q.next
        return p
