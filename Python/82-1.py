#leetcode 讨论区看到的一种JAVA解法，下面是Python版本的实现，非常简洁精彩
#具体原理拿1->2->3->3->4->4->5这个链表推导一下就清楚了。
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
        if(head == None):
            return None
        FakeHead = ListNode(0)
        FakeHead.next = head
        pre = FakeHead
        cur = head
        while (cur!=None):
            while (cur.next != None and cur.val == cur.next.val):
                cur = cur.next
            if (pre.next == cur):
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return FakeHead.next