class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        m = 0
        for i in range(1,len(height)):
            m = max(m, height[i-1])
            max_left[i] = m
        m = 0
        for i in range(len(height)-2, -1, -1):
            m = max(m, height[i+1])
            max_right[i] = m
        s = 0
        for i in range(len(height)):
            diff =  min(max_left[i], max_right[i]) - height[i]
            if diff > 0:
                s += diff
        return s
