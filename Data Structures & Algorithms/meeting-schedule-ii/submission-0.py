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
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        s,e = 0,0
        res,days = 0,0
        while s<n:
            if start[s] < end[e]:
                days += 1
                s += 1
            else:
                days -= 1
                e += 1
            res = max(res,days)

        return res

'''
Sort meetings by end time
Find the max number of meetings doable in 1 day
Then pass the remaining meetings to next day and iterate the same process
Recursion?
'''