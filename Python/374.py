# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        m = (1 + n) // 2
        while (left <= right):
            res = guess(m)
            if res == 0 :
                return m
            elif res == -1:
                right = m - 1
            else :
                left = m + 1
            m = (left + right) // 2