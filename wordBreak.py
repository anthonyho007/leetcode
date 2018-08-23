class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hmap = {}
        def helper(s, wordDict, index):
            if str(index) in hmap:
                return hmap[str(index)] 
            if index >= len(s):
                return True
            for word in wordDict:
                if word == s[index:index + len(word)]:
                    result = helper(s, wordDict, index + len(word))
                    if result == True:
                        return result
            hmap[str(index)] = False
            return False
        return helper(s, wordDict, 0)
