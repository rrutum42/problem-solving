class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force
        # n = len(height)
        # if n == 2:
        #     return min(height[0], height[1])

        # max_water = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         h = min(height[i], height[j])
        #         b = j-i
        #         max_water = max(max_water, h*b)
        # return max_water

        # optimised
        n = len(height)
        if n == 2:
            return min(height[0], height[1])
        
        max_water = 0
        l, r = 0, n-1
        while l < r:
            h = min(height[l], height[r])
            b = r-l
            max_water = max(max_water, h*b)

            if height[l]<=height[r]:
                l +=1
            else:
                r -=1
        return max_water