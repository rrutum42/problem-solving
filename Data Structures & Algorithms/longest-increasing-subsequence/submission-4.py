class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for prev in range(i-1,-2,-1):
                not_take = 0 + dp[i+1][prev+1]
                
                take = 0 
                if (prev == -1 or nums[i]>nums[prev]):
                    take = 1 + dp[i+1][i+1]
                dp[i][prev+1] = max(take,not_take)
        
        return dp[0][-1+1]
        '''
        at each index try to find the longest subsequence
        recursion
        if prev < nums[i] or i == 0: take= 1 + f(i+1,nums[i])
        else nottake= f(i+1,prev)
        return max(take,nottake)
        '''
        # n = len(nums)
        # dp = [[-1]*(n+1) for _ in range(n)]

        # def f(i, prev):
        #     if i == n:
        #         return 0
        #     if dp[i][prev] != -1:
        #         return dp[i][prev]

        #     not_take = 0 + f(i+1,prev)
            
        #     take = 0 
        #     if (prev == -1 or nums[i]>nums[prev]):
        #         take = 1 + f(i+1,i)
        #     dp[i][prev] = max(take,not_take)
        #     return dp[i][prev]
        
        # return f(0,-1)