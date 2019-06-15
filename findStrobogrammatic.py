class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strobo_single = ["0", "1", "8"]
        strobo_pair = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        
        t = n
        
        def recurseStrobo(l_str, r_str, n):
            if n == 0:
                return [l_str + r_str]
            if n == 1:
                ret = []
                for k in strobo_single:
                    ret += recurseStrobo(l_str + k, r_str, n-1)
                return ret
            else:
                ret = []
                for k, v in strobo_pair.items():
                    if k == "0" and t == n:
                        continue
                    ret += recurseStrobo(l_str + k, v + r_str, n - 2)
                return ret
        
        return recurseStrobo("", "", n)

