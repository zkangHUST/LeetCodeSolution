#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (40.74%)
# Total Accepted:    141.4K
# Total Submissions: 347K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        vowel = ['a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        s = list(s)
        while True:
            while(i < j and s[i] not in vowel):
                i += 1
            while(j > i and s[j] not in vowel):
                j -= 1
            if (i < j and s[i] in vowel and s[j] in vowel):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1
            else:
                break
        return ''.join(s)

res = Solution()
ans = res.reverseVowels("bcd")
print(ans)
