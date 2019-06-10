class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if len(haystack) - i < len(needle):
                break
            match = 0
            while match < len(needle) and i+match < len(haystack) and haystack[i+match] == needle[match]:
                match += 1
            if match == len(needle):
                return i
        return -1
