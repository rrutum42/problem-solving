"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # O(nlogn), O(n)
        n = len(intervals)
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        s,e = 0,0
        res,rooms = 0,0
        while s<n:
            # a new meeting starts before the earliest one ends
            if start[s] < end[e]:
                rooms += 1 # need one more room
                s += 1
            else:
                # a meeting has ended
                rooms -= 1 # room is freed
                e += 1
            res = max(res,rooms)

        return res

'''
Sort meetings by end time
Find the max number of meetings doable in 1 day
Then pass the remaining meetings to next day and iterate the same process
Recursion?
=========
intervals = [(0,40),(5,10),(15,20)]

start = [0,5,15]
end = [10,20,40]

s,e=0,0
rooms = 0 

0<10
rooms = 1
s=1
res = 1

5<10
rooms=2
s=2
res=2

!15<10
rooms=1
e=1
res=2

15<20
rooms=2
s=3
res=2

return 2
'''