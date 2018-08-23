class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        i = 0
        ptr = 0
        ctr = 0
        result = 0
        
        total = 0
        for word in sentence:
            total += len(word)
        total += len(sentence)        
        while i < rows:
            if cols - ptr >= total:
                result += (cols-ptr) // total
                ptr = cols - (cols-ptr) % total
            
            wsize = len(sentence[ctr])
            
            if wsize + ptr > cols:
                ptr = 0
                i += 1
            elif wsize + ptr == cols or wsize + ptr + 1 == cols:
                ctr += 1
                ptr = 0
                i += 1
            else:
                ptr = ptr + wsize + 1
                ctr += 1
            
            if ctr == len(sentence): 
                ctr = 0
                result += 1
            
            if ctr == 0 and ptr == 0:
                result = rows // i * result
                rows = rows%i
                i = 0
        return result
