#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }
        roman = ''
        for symbol, val in sorted(lookup.items(), key = lambda t: t[1])[::-1]:
            while num >= val:
                roman += symbol
                num -= val
        return roman
res = Solution()
res.intToRoman(10)