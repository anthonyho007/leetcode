class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        long = ""
        short = ""
        
        if len(s) > len(t):
            short = t
            long = s
        else:
            short = s
            long = t
        
        ctr = 0
        l1 = 0
        s1 = 0
        if abs(len(long) - len(short)) >= 1 :
            return False
        
        if len(short) == 0 and len(long) == 0:
            return False
        
        if len(short) == 0 and len(long) == 1:
            return True
        
        while s1 < len(short):
            if short[s1] == long[l1]:
                s1 += 1
                l1 += 1
            elif ctr == 0:
                l1 += 1
                ctr +=1
                if len(long) == len(short):
                    s1 += 1
            else :
                return False
        
        if ctr == 1:
            return True
        if ctr == 0 and len(long) - s1 == 1:
            return True
        return False
