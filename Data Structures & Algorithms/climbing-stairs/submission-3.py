class Solution:
    def climbStairs(self, n: int) -> int:

        prev2 = 1
        prev1 = 1
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1

        # dp = [-1] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, len(dp)):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        
        # dp = [-1] * (n+1)
        # def climb(n):
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2

        #     if dp[n] != -1:
        #         return dp[n]

        #     dp[n] = climb(n-1) + climb(n-2)    
        #     return dp[n]
        
        # return climb(n)
        
        # dp = [-1] * (n+1)
        # def climb(n):
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2

        #     return climb(n-1)+climb(n-2)
        
        # return climb(n)
        