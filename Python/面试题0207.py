# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = 0, 0
        p1, p2 = headA, headB
        tail1, tail2 = None, None
        while p1:
            l1 += 1
            tail1 = p1
            p1 = p1.next
        while p2:
            l2 += 1
            tail2 = p2
            p2 = p2.next
        
        if tail1 != tail2:
            return None
        p1, p2 = headA, headB
        cnt = 0
        if l1 > l2:
            k = l1 - l2
            # p1 = headA
            # cnt = 0
            while p1:
                cnt += 1
                p1 = p1.next
                if cnt == k:
                    break
                # p1 = p1.next
        elif l1 < l2:
            k = l2 - l1
            # p2 = headB
            # cnt = 0
            while p2:
                cnt += 1
                p2 = p2.next
                if cnt == k:
                    break
                # p2 = p2.next
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None