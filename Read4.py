# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        rem = n
        total = 0
        rbuf = [""] * 4
        
        while rem > 0:
            nread = read4(rbuf)
            rd = min(nread, rem)
            for i in range(rd):
                buf[total] = rbuf[i]
                total += 1
            rem -= rd
            if rd < 4:
                break
        return total
