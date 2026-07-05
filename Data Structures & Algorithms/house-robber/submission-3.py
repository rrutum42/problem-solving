class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        
        return dp[n-1]

        # n = len(nums)
        # dp = [-1] * (n + 1)

        # def rob(i):
        #     if i >= n:
        #         return 0 
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = max(nums[i]+rob(i+2), rob(i+1))
        #     return dp[i]
        
        # return rob(0)

        '''
        recursion 
        max(rob i + recursion on rob i + 2, rob i+1) 

        '''
        # n = len(nums)
        # def rob(i):
        #     if i >= n:
        #         return 0 

        #     return max(nums[i]+rob(i+2), rob(i+1))
        
        # return rob(0)