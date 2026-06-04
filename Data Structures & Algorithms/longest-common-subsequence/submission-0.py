class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # tabulation
        n = len(text1)
        m = len(text2)
        dp = [[0 for j in range(m+1)]
                for i in range(n+1)]
        # for i in range(n):
        #     dp[i][0] = 0
        # for j in range(m):
        #     dp[0][j] = 0
        
        for i in range(1, n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] =  1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
        
        # # memoization
        # dp = [[-1 for j in range(len(text2))]
        #          for i in range(len(text1))]
        # def f(i,j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if text1[i] == text2[j]:
        #         return 1 + f(i-1,j-1)
            
        #     dp[i][j] = max(f(i-1,j),f(i,j-1))
        #     return dp[i][j] 

        # i,j = len(text1)-1, len(text2)-1
        # return f(i,j)
'''
1. index -> i,j
2. check if equal, if not then check all paths i-1 or j-1 match
3. return sum of all paths
'''        
        