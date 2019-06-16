# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        dumpy = ListNode(0)
        dumpy.next = head
        while head:
            length += 1
            head = head.next
        cur = dumpy.next
        tail = dumpy
        size = 1
        while size < length:
            while cur:
                l = cur
                r = self.spilt(cur, size)
                cur = self.spilt(r, size)
                tail.next, tmp = self.merge(l, r)
                tail = tmp
            cur = dumpy.next
            tail = dumpy
            size *= 2
        return dumpy.next

    def spilt(self, head, n):
        n -= 1
        while n and head:   
            n -= 1 
            head = head.next
        if head:
            tmp = head.next
            head.next = None
        else:
            tmp = None
        return tmp
    
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
            
        while tail.next:
            tail = tail.next
        
        return dumpy.next, tail 
    