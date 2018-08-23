class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {}
        def helper(s, index):
            if str(index) in hmap:
                return hmap[str(index)]
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            decode = helper(s, index+1)
            hmap[str(index+1)] = decode
            if index + 1 < len(s):
                if int(s[index:index+2]) < 27:
                    temp = helper(s, index+2)
                    hmap[str(index+2)] = temp
                    decode += temp
            
            return decode
        
        return helper(s, 0)
