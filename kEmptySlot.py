class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i]-1] = i + 1
        
        l = 0
        r = k + 1
        result = len(flowers) + 1
        while r < len(flowers):
            i = l + 1
            while i < r:
                if days[i] < days[l] or days[i] <= days[r]:
                    break
                else:
                    i += 1
            if i == r:
                result = min(result, max(days[l], days[r]))
            l = i 
            r = k + l + 1
        return result if result != len(flowers) + 1 else -1
