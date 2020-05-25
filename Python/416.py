class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        old = {0}
        new = set()
        for v in nums:
            # new = old 
            for n in old:
                if n + v == target:
                    return True
                new.add(n + v)
            old |= new
            new.clear()
        return False
