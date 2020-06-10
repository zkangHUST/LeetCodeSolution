# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        ans = []
        cur = [tree]
        while len(cur) > 0:
            ans.append(self.getList(cur))
            p = []
            for node in cur:
                if node.left:
                    p.append(node.left)
                if node.right:
                    p.append(node.right)
            cur = p
        return ans

    def getList(self, l):
        if not l:
            return None
        head = ListNode(0)
        tail = head
        for i in range(len(l)):
            p = ListNode(l[i].val)
            tail.next = p
            tail = tail.next
        return head.next