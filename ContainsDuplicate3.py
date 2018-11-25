class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int index range
        :type t: int number range
        :rtype: bool
        """
        if len(nums) == 0 or k < 0 or t < 0:
            return False
        minValue = 9999999
        maxValue = -9999999
        
        for num in nums:
            minValue = min(minValue, num)
            maxValue = max(maxValue, num)
        
        comp_range = t + 1
        
        bucket_num = (maxValue -minValue) / comp_range + 1
        
        hp = {}
        
        for i in range(len(nums)):
            ind = (nums[i] - minValue) / comp_range
            
            if ind in hp:
                return True
            
            if ind - 1 >= 0 and ind - 1 in hp and abs(hp[ind-1] - nums[i]) <= t:
                return True
            if ind + 1 < bucket_num and ind+1 in hp and abs(hp[ind+1] - nums[i]) <= t:
                return True
            
            hp[ind] = nums[i]
            
            if i >= k:
                hp.pop((nums[i-k] - minValue)/comp_range)
        return False
                
        
        
