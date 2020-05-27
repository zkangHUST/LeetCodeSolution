class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"
        s = []
        for n in nums:
            s.append(str(n))

        def comp(a, b):
            x, y = a + b, b + a
            if x < y:
                return 1
            elif x > y:
                return -1
            return 0
        s = sorted(s, key=functools.cmp_to_key(comp))
        return "".join(s)
                

