class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # TC O(n), SC O(n)
        n = len(intervals)
        
        i = 0
        res = []
        # find the left non overlapping intervals, prevend < newstart
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i +=1

        # find and merge overlapping intervals, nextstart < newend
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i = i + 1
        
        res.append(newInterval)

        # insert right
        while i<n:
            res.append(intervals[i])
            i +=1
        
        return res
'''
find out the left intervals and right intervals 
find out the overlapping intervals
for left sotre as is
for right store as is
left overlap -> previous end > curr start -> interval(1,3), newInt(2,5)
right overlap -> curr end > next start -> interval(4,9), newInt(2,5)
merge the overlaps
start is min of all starts
end is max of all ends
'''
        