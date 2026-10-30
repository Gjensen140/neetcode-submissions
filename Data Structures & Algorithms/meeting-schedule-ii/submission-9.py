"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)

        if n == 0:
            return 0
        
        starts = intervals.copy()
        ends = intervals.copy()

        starts.sort(key = lambda x: x.start)
        ends.sort(key = lambda x: x.end)

        s = 0
        e = 0

        count = 0
        output = 0
        
        while s < n and e < n:
            t1 = starts[s].start
            t2 = ends[e].end
            if t1 < t2:
                count += 1
                s += 1
            elif t1 == t2:
                e += 1
                s += 1
            else:
                e += 1
                count -= 1

            output = max(count, output)

        return output