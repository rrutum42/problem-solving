class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # tabulation space optimised
        # store values of the previous row
        prev = [0] * n 
        for i in range(m):
            # initialiase current row as 0
            cur = [0] * n
            for j in range(n):
                if i==0 and j == 0:
                    cur[j] = 1
                else:
                    up, left = 0,0
                    if i > 0: up = prev[j]
                    if j > 0: left = cur[j-1]
                    cur[j] = up + left
            prev = cur

        return prev[n-1]
        # # tabulation

        # dp = [[-1 for j in range(n)]
        #         for i in range(m)]
        # dp[0][0] = 1 
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 and j == 0:
        #             dp[i][j]
        #         else:
        #             up, left = 0,0
        #             if i > 0: up = dp[i-1][j]
        #             if j > 0: left = dp[i][j-1]
        #             dp[i][j] = up + left

        # return dp[m-1][n-1]        

        # # memoization
        # dp = [[-1 for j in range(n)]
        #     for i in range(m)]
        # def f(i,j):
        #     # reach 0,0 from m-1,n-1
        #     if i == 0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0 :
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     up = f(i-1,j)
        #     left =  f(i,j-1)
        #     dp[i][j] = up + left
        #     return dp[i][j]

        
        # return f(m-1,n-1)
        