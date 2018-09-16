# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if(len(nums) == 0):
            return None
        root = TreeNode(0)
        root.left = None
        root.right = None
        if (len(nums) == 1):
            root.val = nums[0]
            root.left = None
            root.right = None
        else:
            root.val = max(nums)
            p  = nums.index(root.val)
            root.left = self.constructMaximumBinaryTree(nums[0:p])
            root.right = self.constructMaximumBinaryTree(nums[p+1:])
        return root
    def levelOrderTravel(self,root):
        queue = []
        if (root == None):
            return 
        else:
            queue.append(root)
        while(len(queue) != 0):
            cur = queue[0]
            if (cur != None):
                print("%s->"%(cur.val))
            if (cur.left != None):
                queue.append(cur.left)
            if (cur.right != None):
                queue.append(cur.right)
            del queue[0]
        


res = Solution()
nums = [3,2,1,6,0,5]
ans = res.constructMaximumBinaryTree(nums)
res.levelOrderTravel(ans)


