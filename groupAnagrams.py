class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = {}
        
        for word in strs:
            s = str(sorted(word))
            if s not in hmap:
                hmap[s] = []
            hmap[s].append(word)
        
        result = []
        for k in hmap:
            result.append(hmap[k])
        
        return result
