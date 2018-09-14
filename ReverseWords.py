class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(lst , s, e):
            while s < e:
                lst[s], lst[e] = lst[e], lst[s]
                s += 1
                e -= 1
        s1 = str
        
        # do one reverse on the entire string and then reverse each word
        reverse(s1, 0, len(str)-1)
        i = 0
        e = 0
        while e < len(str):
            if s1[e] != ' ':
                e += 1
            else:
                reverse(s1, i, e-1)
                i = e + 1
                e = e + 1
                
        reverse(s1, i, e-1)
