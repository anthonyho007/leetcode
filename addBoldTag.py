class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        start = False
        end = -1
        result = ""
        for i in range(len(s)):
            for word in dict:
                if i+ len(word)-1 <= len(s) and s[i:i+len(word)] == word:
                    if start == False:
                        result += "<b>"
                        start = True
                    end = max(i + len(word)-1, end)
            if i > end and start == True:
                result += "</b>"
                start = False
            result += s[i]
        if start == True:
            result += "</b>"
        
        return result
        
