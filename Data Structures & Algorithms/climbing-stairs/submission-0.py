class Solution:
    def climbStairs(self, n: int) -> int:
        # tabulation space optimised: O(n), O(1)
        # we need only i-2,i-1 and curi
        prev2 = 1
        prev1 = 1
        for i in range(2,n+1):
            curi = prev1 + prev2
            prev2 = prev1
            prev1 = curi
        return prev1

        # # tabulation: O(n), O(n) - dp array
        # dp = [-1] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,len(dp)):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        
        # # memoization: O(n), O(n) - recursion stack space + O(n) - dp array
        # idx = n
        # dp = [-1] * (n + 1)
        # def climb(n):
        #     if n <= 1:
        #         return 1
        #     if dp[n] != -1:
        #         return dp[n]
        #     single = climb(n-1) 
        #     double = climb(n-2) 
        #     dp[n] = single + double
        #     return dp[n]
        # return climb(idx)

        # recursion
        # idx = n
        # def climb(n):
        #     if n == 0:
        #         return 1
        #     if n == 1:
        #         return 1
        #     single = climb(n-1) 
        #     double = climb(n-2) 
        #     return single + double 
        
        # return climb(idx)
        