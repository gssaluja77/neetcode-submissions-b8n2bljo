"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()

        i, j = 0, 0
        on_going = 0
        res = 0

        while i < len(start):
            if start[i] < end[j]:
                on_going += 1
                res = max(res, on_going)
                i += 1
            else:
                j += 1
                on_going -= 1
        return res