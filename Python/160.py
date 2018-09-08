# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        posA = headA
        posB = headB

        lenA = self.getLen(headA)
        lenB = self.getLen(headB)

        if (lenA - lenB > 0):
            i = 0
            while( i < lenA - lenB):
                posA = posA.next
                i += 1                
        elif (lenB - lenA > 0): 
            i = 0
            while( i < lenB - lenA):
                posB = posB.next
                i += 1 
        
        while(posA != posB):
            posA = posA.next
            posB = posB.next
        return posA
    def getLen(self,headA):
        if (headA == None):
            return 0
        len = 0
        while (headA) :
            len += 1
            headA = headA.next
        return len


