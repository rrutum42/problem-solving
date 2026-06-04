"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            curr = intervals[i]

            if prev.end > curr.start:
                return False
        return True
            
'''
find count of non overlapping meetings
if count = len of intervals return true else false

sort all acc to the end values, pick the 
'''