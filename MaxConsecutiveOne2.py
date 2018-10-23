class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        cnt = 0
        max1 = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
            
            if cnt == 2:
                while nums[start] == 1:
                    start += 1
                start += 1
                cnt -= 1
            max1 = max(max1, i - start + 1)
        
        return max1
