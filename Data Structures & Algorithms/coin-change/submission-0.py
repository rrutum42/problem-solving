class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # tabulation
        dp = [[-1]*(amount+1) for _ in range(len(coins))]

        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = int(i/coins[0])
            else:
                dp[0][i] = 1e9
        
        for idx in range(1, len(coins)):
            for T in range(amount+1):
                not_take = dp[idx-1][T]
                take = 1e9
                if coins[idx] <= T:
                    take = 1 + dp[idx][T-coins[idx]]
                dp[idx][T] = min(take,not_take)

        ans = dp[len(coins)-1][amount]
        if ans >= 1e9:
            return -1
        return ans

        # #memoization O(T*n), O(T*n)
        # dp = [[-1]*(amount+1) for _ in range(len(coins))]
        # def f(idx,T):
        #     if idx == 0:
        #         if T%coins[idx] == 0 :
        #             return int(T/coins[idx])
        #         else:
        #             return 1e9

        #     if dp[idx][T] != -1:
        #         return dp[idx][T]

        #     not_take = 0 + f(idx-1, T)
        #     take = 1e9
        #     if coins[idx] <= T:
        #         take = 1 + f(idx, T-coins[idx])
        #     dp[idx][T] = min(not_take,take)    
        #     return dp[idx][T]
        
        # ans = f(len(coins)-1,amount) 
        # if ans >= 1e9:
        #     return -1
        # return ans 

        # # recursion
        # def f(idx,T):
        #     if idx == 0:
        #         if T%coins[idx] == 0 :
        #             return int(T/coins[idx])
        #         else:
        #             return 1e9

        #     not_take = 0 + f(idx-1, T)
        #     take = 1e9
        #     if coins[idx] <= T:
        #         take = 1 + f(idx, T-coins[idx])
        #     return min(not_take,take)
        
        # ans = f(len(coins)-1,amount) 
        # if ans >= 1e9:
        #     return -1
        # return ans 
