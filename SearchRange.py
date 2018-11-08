class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0
        end = len(nums) -1
        ind1, ind2 = -1, -1
        while start <= end:
            m = start + (end - start) // 2
            if nums[m] > target:
                end = m -1
            elif nums[m] < target:
                start = m + 1
            else:
                end = m - 1
        if start >= 0 and start < len(nums) and nums[start] == target:
            ind1 = start
        start = 0
        end = len(nums) -1
        while start <= end:
            m = start + (end - start) // 2
            if nums[m] > target:
                end = m -1
            elif nums[m] < target:
                start = m + 1
            else:
                start = m + 1
        
        if end >= 0 and end < len(nums) and nums[end] == target:
            ind2 = end
        
        return [ind1, ind2]
