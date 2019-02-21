# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fakeHead = ListNode(0)
        fakeHead.next = head
        self.swap(fakeHead)
        return fakeHead.next
    def swap(self, head):
        if (head.next and head.next.next):
            tmp1 = head.next.next.next
            head.next.next.next = head.next;
            tmp2 = head.next
            head.next = head.next.next
            tmp2.next = tmp1
            self.swap(head.next.next)