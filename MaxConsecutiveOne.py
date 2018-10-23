class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        start = -1
        op = False
        
        for i in range(len(nums)):
            if nums[i] == 1 and op == False:
                start = i
                op = True
            elif nums[i] == 0 and op == True:
                op = False
                max1 = max(max1, i-start)
        if op == True:
            max1 = max(max1, len(nums) - start)
        return max1
