class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TC O(nlogn) + O(n) SC O(n)
        intervals.sort()
        # intervals.sort(key= lambda i: i[0])
        n = len(intervals)
        res = []

        for i in intervals:
            if not res:
                res.append(i)
                continue
            
            prev_end = res[-1][1]
            if prev_end >= i[0]:
                res[-1][1] = max(prev_end, i[1])
            else:
                res.append(i)
        return res