#!/usr/bin/env python

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def cmpStr(s1, s2, start, end):
            if len(s1) > len(s2):
                return False
            while start < end:
                if s1[start] == s2[start]:
                    start += 1
                else:
                    return False
            return True
        def helper(s, index, wordDict, memo):
            if s[index:] in memo:
                return memo[s[index:]]
            if index >= len(s):
                return True
            for word in wordDict:
                lgt = index + len(word)
                if cmpStr(word,s[index:lgt], 0, len(word)):
                    print word
                    if helper(s, lgt, wordDict, memo):
                        memo[s[index:]] = True
                        return True
            memo[s[index:]] = False
            return False
        memo = {}
        return helper(s, 0, wordDict, memo)
