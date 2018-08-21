#!/usr/bin/env python

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class TimePoint(object):
    def __init__(self, time = 0, entry = None):
        self.time = time
        self.entry = entry

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        N = len(intervals)
        if N == 0:
            return 0

        times = []
        for interval in intervals:
            times.append(TimePoint(interval.start, "s"))
            times.append(TimePoint(interval.end, "e"))

        times = sorted(times, key=lambda x:(x.time, x.entry))

        ctr = 0
        max_room = 1
        for time in times:
            if time.entry == "s":
                ctr += 1
                max_room = max(max_room, ctr)
            else:
                ctr -= 1

        return max_room


