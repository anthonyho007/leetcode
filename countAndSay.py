class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def count(seq):
            res = ""
            i = 0
            n = len(seq)
            cnt = 1
            
            while i < n:
                if i + 1 < n and seq[i+1] == seq[i]:
                    cnt += 1
                else:
                    res += str(cnt)
                    res += seq[i]
                    cnt = 1
                i += 1
            return res
        seq = "1"
        for i in range(n-1):
            print seq
            seq = count(seq)
        return seq