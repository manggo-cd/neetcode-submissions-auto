"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals mean that the prev end is leq to the next start

        # so we can first sort by start times
        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            prevEnd, currStart = intervals[i-1].end, intervals[i].start

            if prevEnd > currStart:
                return False

        return True