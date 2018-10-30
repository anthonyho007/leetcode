class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        h = x
        if x <= 1:
            return x
        
        while l <= h:
            m =  l + (h - l) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m +1
            else:
                h = m -1 
        return h
        
