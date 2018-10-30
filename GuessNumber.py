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
        l,h = 1, n
        
        while l <= h:
            m = l + (h - l) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res  == 1:
                l = m + 1
            else:
                h = m - 1
        return -1
            
