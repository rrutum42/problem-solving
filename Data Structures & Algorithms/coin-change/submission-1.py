class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        tabulation
        '''
        dp = [[-1]*(amount + 1) for _ in range(len(coins))]

        # base case
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = int(i/coins[0])
            else:
                dp[0][i] = 1e9

        for idx in range(1, len(coins)):
            for T in range(amount + 1):
                notTake = dp[idx-1][T]
                take = 1e9
                if coins[idx] <= T:
                    take = 1 + dp[idx][T - coins[idx]]
                
                dp[idx][T] = min(take, notTake)

        ans = dp[len(coins)-1][amount]
        if ans >= 1e9:
            return -1
        return ans
        '''
        memoization
        '''    
        # dp = [[-1]*(amount + 1) for _ in range(len(coins))]
        # def f(i, T):
        #     # base case
        #     if i == 0:
        #         if T%coins[i] == 0:
        #             return int(T/coins[i])
        #         else:
        #             return 1e9
        #     if dp[i][T] != -1:
        #         return dp[i][T]
        #     # explore all scenarios
        #     notTake = f(i-1, T)
        #     take = 1e9
        #     if coins[i] <= T:
        #         take = 1 + f(i,T-coins[i])
        #     dp[i][T] = min(take, notTake)
        #     return dp[i][T]
        
        # ans = f(len(coins)-1, amount)
        # if ans >= 1e9:
        #     return -1
        # return ans

        '''
        recursion
        fn
            base case
            try all ways
            return ans 
        '''
        # def f(i, T):
        #     # base case
        #     if i == 0:
        #         if T%coins[i] == 0:
        #             return int(T/coins[i])
        #         else:
        #             return 1e9
        #     # explore all scenarios
        #     notTake = f(i-1, T)
        #     take = 1e9
        #     if coins[i] <= T:
        #         take = 1 + f(i,T-coins[i])
        #     return min(take, notTake)
        
        # ans = f(len(coins)-1, amount)
        # if ans >= 1e9:
        #     return -1
        # return ans

        # ================striver ^===    
        # memo = {}
        
        # def dfs(target):
        #     if target == 0:
        #         return 0
        #     if target in memo:
        #         return memo[target]

        #     res = 1e9
        #     for coin in coins:
        #         if target - coin >=0:
        #             res = min(res,1+dfs(target-coin))
        #     memo[amount] = res
        #     return res
        
        # minCoins = dfs(amount)
        # return -1 if minCoins >= 1e9 else minCoins

        # def dfs(target):
        #     if target == 0:
        #         return 0

        #     res = 1e9
        #     for coin in coins:
        #         if target -coin >=0:
        #             res = min(res,1+dfs(target-coin))
        #     return res
        
        # minCoins = dfs(amount)
        # return -1 if minCoins >= 1e9 else minCoins
        