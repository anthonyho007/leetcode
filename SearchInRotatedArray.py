class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findPivot(arr, start, end):
            if start > end:
                return -1
            if start == end:
                return end
            m = (start + end) / 2
            if m+1 <= end and arr[m] > arr[m+1]:
                return m
            if m-1 >= start and arr[m-1] > arr[m]:
                return m-1
            if arr[m] > arr[start]:
                return findPivot(arr, m+1, end)
            else:
                return findPivot(arr, start, m-1)
        
        def binarySearch(arr, start, end, value):
            if start > end:
                return -1
            m = (start + end) / 2
            if arr[m] == value:
                return m
            if arr[m] > value:
                return binarySearch(arr, start, m-1, value)
            else:
                return binarySearch(arr, m+1, end, value)
        
        n = len(nums) -1
        pivot = findPivot(nums, 0, n)
        print(pivot)
        if pivot == -1:
            return binarySearch(nums, 0, n, target)
        
        left = binarySearch(nums, 0, pivot, target)
        if left != -1:
            return left
        else:
            return binarySearch(nums, pivot+1, n, target)
