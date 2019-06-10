class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[size] = nums[i]
                size += 1
        return size

