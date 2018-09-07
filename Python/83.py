# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        q = ListNode(0)
        p = head
        #注意head可能为空
        if(head != None and head.next != None):
            q = head.next
        else:
            return head
        while(q!=None):
            if(p.val == q.val):
                p.next = q.next
                q=p.next
            else:
                p=p.next
                q=p.next
        return head