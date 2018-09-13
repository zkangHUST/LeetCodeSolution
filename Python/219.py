class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        if(k >= length):
            l = set(nums)
            if(length != len(l)):
                return True
            else:
                return False
                        
        for i in range(length-k):
            l = set(nums[i:i+k+1])
            if(len(l)!=k+1):
                return True
        
        return False
