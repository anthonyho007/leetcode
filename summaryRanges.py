class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        result = []
        if len(nums) == 0:
            return result
        
        start = nums[0]
        prev = nums[0]
        
        i = 1
        while i < len(nums):
            if nums[i] == prev + 1:
                prev = nums[i]
                i += 1
            else:
                if start == prev:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(prev))
                start = nums[i]
                prev = nums[i]
                i += 1
                
        if start == prev:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(prev))
            start = nums[i-1]
            prev = nums[i-1]
        
        return result
