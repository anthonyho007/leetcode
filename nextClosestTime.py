class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        times = []
        for i in range(len(time)):
            if time[i] != ':':
                times.append(int(time[i]))
        nums = sorted(set(times))
        
        result =  ""
        index = 3
        
        while index >= 0:
            if index == 3:
                for num in nums:
                    if times[index] < num:
                        return time[:index+1] + str(num)
                result = str(nums[0]) + result
                index -= 1
            if index == 2:
                limit = 6
                for num in nums:
                    if num > times[index] and num < limit:
                        return time[:index+1] + str(num) + result
                result = ":" + str(nums[0]) + result
                index -= 1
            if index == 1:
                if time[0] == '2':
                    limit = 4
                else:
                    limit = 10
                
                for num in nums:
                    if num > times[index] and num < limit:
                        return time[:index] + str(num) + result
                result = str(nums[0]) + result
                index -= 1
            if index == 0:
                limit = 3
                for num in nums:
                    if num > times[index] and num < limit:
                        return time[:index] + str(num) + result 
                result = str(nums[0]) + result
                index -= 1
        
        return result
