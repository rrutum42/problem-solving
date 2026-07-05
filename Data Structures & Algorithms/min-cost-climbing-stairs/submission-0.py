class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
        
        return dp[n]

        # dp = [-1] * len(cost)

        # def climb(n):
        #     if n> len(cost) - 1:
        #         return 0

        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] = cost[n] + min(climb(n+1), climb(n+2))     
        #     return dp[n]
        

        # return min(climb(0), climb(1))
        
        # def climb(n):
        #     if n> len(cost) - 1:
        #         return 0
                
        #     return cost[n] + min(climb(n+1), climb(n+2))
        

        # return min(climb(0), climb(1))
        