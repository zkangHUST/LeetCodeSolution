class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        nums = {"I":1, "V":5, "X":10,"L":50, "C":100, "D": 500, "M":1000}
        value = 0
        l = len(s)
        for i in range(l):
            if i < l - 1 and nums[s[i]] < nums[s[i + 1]]:
                value -= nums[s[i]]
            else:
                value += nums[s[i]]
        return value    