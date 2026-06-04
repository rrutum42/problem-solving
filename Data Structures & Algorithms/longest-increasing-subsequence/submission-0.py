class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # memoization
        n = len(nums)
        
        # idx goes from 0 to n-1 -> n size
        # prev goes from -1 to n -1 -> m size
        # to accomodate the nXm array we need to coordinate change 
        dp = [[-1]*(n+1) for _ in range(n)]

        def f(idx, prev):
            if idx == n:
                return 0
            if dp[idx][prev] != -1:
                return dp[idx][prev]
            # if you don't take the idx moves and prev remains the same
            not_take = 0 + f(idx+1,prev)
            # if you take then pick the max
            take = 0
            if (prev == -1 or nums[idx]>nums[prev]):
                take = 1 + f(idx+1,idx)
            dp[idx][prev] = max(take, not_take)
            return dp[idx][prev]

        return f(0,-1)
        
        # # recursion
        # n = len(nums)

        # def f(idx, prev):
        #     if idx == n:
        #         return 0
            
        #     # if you don't take the idx moves and prev remains the same
        #     not_take = 0 + f(idx+1,prev)
        #     # if you take then pick the max
        #     take = 0
        #     if (prev == -1 or nums[idx]>nums[prev]):
        #         take = 1 + f(idx+1,idx)
        #     len = max(take, not_take)
        #     return len

        # return f(0,-1)    
'''
For subsequence you can either take or not take the element
'''            
        