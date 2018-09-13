class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        start = 0
        curr = 1
        while curr != len(nums):
            if nums[curr] != nums[start]:
                nums[start+1] = nums[curr]
                start += 1
            else:
                curr += 1
        
        return start + 1
