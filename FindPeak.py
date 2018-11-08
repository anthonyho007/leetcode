class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)
        
        while start < end:
            m = start + (end - start) // 2
            if m + 1 < len(nums) and nums[m+1] > nums[m]:
                start = m + 1
            else:
                end = m
        return start
