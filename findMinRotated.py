class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        
        while start < end:
            m = start + (end - start) // 2
            if nums[m] > nums[end] and nums[m] >= nums[start]:
                start = m+1
            else:
                end = m
        return nums[start]
