# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        slow = head
        fast = head.next
        while(fast and fast.next): 
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))
    
    def merge(self, l1, l2):
        dumpy = ListNode(0)
        tail = dumpy
        while(l1 and l2):
            if l1.val > l2.val:
                l1, l2 = l2, l1
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        if l1:
            tail.next = l1
        
        if l2:
            tail.next = l2
        return dumpy.next
    
                 