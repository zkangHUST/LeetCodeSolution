# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        FakeHead = ListNode(0)
        FakeHead.next = l1
        pre = FakeHead
        cur = pre.next
        n = l2
        while(cur!= None and n != None):
            if(cur.val > n.val):
                temp = n
                n = n.next
                temp.next = cur
                pre.next = temp      
                pre= pre.next
            else:
                pre = cur
                cur = cur.next
        if(n!=None):
            pre.next = n
        return FakeHead.next
                