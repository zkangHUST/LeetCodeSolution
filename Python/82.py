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
        if(head == None or head.next == None):
            return head       
        root = ListNode(0)
        root.next = head
        p = root
        m = p.next
        n = m.next
        flag = 0
        while(m and n):
            if (m.val == n.val):
                temp = m.val
                n = n.next
                m.next = n
                flag = 1
            elif(flag ==1 and m.val == temp):
                m = n
                n = n.next
                p.next = m
            else: 
                flag = 0
                p = m
                m = p.next
                n = m.next
        if(flag ==1 and m.val == temp):
            m = n
            p.next = m
        return root.next