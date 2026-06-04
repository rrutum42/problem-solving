class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda i: i[1])

        non_o = 1
        lastEnd = intervals[0][1]
        for i in range(1, n):
            if lastEnd <= intervals[i][0]:
                non_o +=1
                lastEnd = intervals[i][1]
        
        return n - non_o
'''
Find the max num of intervals we can get which are non overlapping
len - non overlapping is ans
'''