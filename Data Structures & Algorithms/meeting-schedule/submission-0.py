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

        intervals.sort(key = lambda i : i.start)
        
        for i in range(1, n):
            m1 = intervals[i - 1]
            m2 = intervals[i]

            if m1.end >= m2.end or m1.end > m2.start:
                return False
            
        return True