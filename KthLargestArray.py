class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, start, end):
            tmp = nums[end]
            i = start-1
            e = end
            for x in range(start,end):
                if nums[x] < tmp:
                    i += 1
                    nums[i], nums[x] = nums[x], nums[i]
            
            nums[i+1], nums[end] = nums[end],nums[i+1]
            return i+1
        k = len(nums) -k
        piv = -1
        n = len(nums)-1
        start = 0
        end = n
        while piv != k:
            piv = partition(nums,start,end)
            if piv < k:
                start = piv + 1
            elif piv > k:
                end = piv-1
            else:
                break

        return nums[piv]
