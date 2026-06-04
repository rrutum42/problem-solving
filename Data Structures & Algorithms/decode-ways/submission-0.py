class Solution:
    def numDecodings(self, s: str) -> int:
        # tabulation space optimised
        n = len(s)
        dp1 = 1
        dp = dp2 = 0
        for i in range(n-1,-1,-1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1

            if (i + 1 < len(s)) and (s[i] == '1' or (s[i]== '2' and s[i+1] < '7')):
                    dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
        # # tabulation
        # n = len(s)

        # dp = [-1 for _ in range(n+1)]
        # dp[n] = 1

        # for i in range(n-1,-1,-1):
        #     if s[i] == '0':
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i+1]

        #     if (i + 1 < len(s)) and (s[i] == '1' or (s[i]== '2' and s[i+1] < '7')):
        #             dp[i] += dp[i+2]
        
        # return dp[0]

        # # memoization
        # n = len(s)

        # dp = [-1 for _ in range(n)]

        # def dfs(i):
        #     if i == n:
        #         return 1
        #     if s[i] == '0':
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     res = dfs(i+1)
        #     if i < n -1:
        #         # check if a valid num from 1 to 26 can be made
        #         if (s[i] == '1' or (s[i]== '2' and s[i+1] < '7')):
        #             res += dfs(i+2)
        #     dp[i] = res
        #     return res
        
        # return dfs(0)

        # recursion
        # n = len(s)

        # def dfs(i):
        #     if i == n:
        #         return 1
        #     if s[i] == '0':
        #         return 0
            
        #     res = dfs(i+1)
        #     if i < n -1:
        #         # check if a valid num from 1 to 26 can be made
        #         if (s[i] == '1' or (s[i]== '2' and s[i+1] < '7')):
        #             res += dfs(i+2)

        #     return res
        
        # return dfs(0)
        