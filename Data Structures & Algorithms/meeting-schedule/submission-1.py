"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key = lambda x: x.start)

        highest = float('-inf')

        for i in range(n):
            if intervals[i].start < highest:
                return False
            
            highest = max(intervals[i].end, highest)

        return True