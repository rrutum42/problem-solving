class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(logn), O(n)
        intervals.sort(key=lambda pair: pair[0])

        merged = [intervals[0]]

        for start,end in intervals:
            lastEnd = merged[-1][1]

            if start <= lastEnd:
                merged[-1][1] = max(lastEnd, end)
            else:
                merged.append([start,end])

        return merged
        