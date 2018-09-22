# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fakeHead = ListNode(0)
        fakeHead.next = head
        p = q = fakeHead
        for i in range(n):
            p = p.next
        while(p.next!=None):
            p=p.next
            q=q.next
        q.next = q.next.next
        return fakeHead.next
