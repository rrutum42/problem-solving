# https://www.youtube.com/watch?v=Bzat9vgD0fs 
# TC: O(n)
# SC: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        brute force. for each elem find the previous smaller elem(pse) and next smaller elem(nse).
        area = height(i) *(nse-pse-1)
        optimised:
        instead of doing two pass to calc pse and nse we can calc it in one pass
        maintain monotonic stk
        for each elem i if heights[stk top] >= heights[i]
            h = pop from stk
            update the height for the popped elem
            maxA = max(maxA, h * (i-stk.top-1)) 
        stk.push()
        '''
        stk = []
        maxArea = 0
        n = len(heights)

        for i in range(n+1):
            while stk and (i==n or heights[i] <= heights[stk[-1]]):
                height = heights[stk.pop()]
                width = i if not stk else i - stk[-1] -1
                maxArea = max(maxArea, height* width)
            stk.append(i)
        
        return maxArea