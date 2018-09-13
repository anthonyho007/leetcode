class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) -1
        curr = 0
        
        while curr <= end:
            if nums[curr] == 0:
                nums[curr], nums[start] = nums[start], nums[curr]
                curr += 1
                start += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
