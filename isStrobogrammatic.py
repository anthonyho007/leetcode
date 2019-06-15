class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strobo_pair = {'0':"0", "1":"1", "6":"9", "9":"6", "8":"8"}
        strobo_single = ["0", "1", "8"]
        
        e = len(num) -1
        s = 0
        
        while s <= e:
            if s == e:
                if not num[s] in strobo_single:
                    return False
            else:
                if num[s] not in strobo_pair or strobo_pair[num[s]] != num[e]:
                    return False
            s += 1
            e -= 1
        return True
