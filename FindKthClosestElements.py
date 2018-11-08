class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        start, end = 0, len(arr) -1
        val = -1
        result = []
        while start + 1 < end:
            m = start + (end - start) // 2
            if arr[m] > x:
                end = m
            elif arr[m] < x:
                start = m
            else:
                val = m
                break
        
        ctr = k
        if val != -1:
            left, right = val -1, val +1
            ctr -= 1
            result.append(arr[val])
        else:
            left, right = start, end
        while ctr > 0:
            if left >= 0 and right < len(arr):
                if x - arr[left] <= arr[right] - x:
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            elif left >= 0:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            ctr -= 1
        return sorted(result)
                    
            
