# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # 在hashset中查找的效率是O(1)
        l = set(G)
        key = head
        ans = 0
        while (key != None):
            if(key.val in l):
                ans += 1
                while(key != None and key.val in l):
                    key = key.next
            else:
                key = key.next
        return ans

        