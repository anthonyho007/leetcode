class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        extra = True
        ptr = len(digits) -1
        while extra == True and ptr >= 0:
            digits[ptr] += 1
            if digits[ptr] < 10:
                extra = False
                break
            digits[ptr] = 0
            ptr -= 1
        if extra == True:
            digits = [1] + digits
        return digits
