class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = set()
        
        hmap = {}
        
        for num in nums1:
            if str(num) not in hmap:
                hmap[str(num)] = num
        
        for num in nums2:
            if str(num) in hmap:
                result.add(num)
        
        return list(result)
