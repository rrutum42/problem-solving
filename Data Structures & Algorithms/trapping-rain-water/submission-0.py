class Solution:
    def trap(self, height: List[int]) -> int:
        # # O(n), O(n)
        # n = len(height)

        # if n == 0:
        #     return 0

        # leftMax = [0] * n
        # rightMax = [0] * n

        # leftMax[0] = height[0]
        # rightMax[n-1] = height[n-1]
        # for i in range(1,n):
        #     leftMax[i] = max(leftMax[i-1],height[i])
        
        # for i in range(n-2, -1, -1):
        #     rightMax[i] = max(rightMax[i+1],height[i])

        # print(leftMax)
        # print(rightMax)
        
        # res = 0
        # for i in range(n):
        #     res += min(leftMax[i],rightMax[i]) - height[i]
        # return res
        # trapped water at index i is given by: min(height[l], height[r]) - height[i]
        # We can store the prefix maximum in an array by iterating from left to right and the suffix maximum in another array by iterating from right to left. For example, in [1, 5, 2, 3, 4], for the element 3, the prefix maximum is 5, and the suffix maximum is 4. Once these arrays are built, we can iterate through the array with index i and calculate the total water trapped at each position using the formula: min(prefix[i], suffix[i]) - height[i].

        # O(n), O(1)
        if not height:
            return 0
        
        n = len(height)
        l, r = 0, n-1
        leftMax, rightMax = height[l],height[r]
        res = 0
        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res



        