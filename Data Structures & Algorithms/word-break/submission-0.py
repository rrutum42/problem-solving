class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # tabulation 

        wordSet = set(wordDict)
        dp = [False]*(len(s)+1)
        
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=True
                    break
        return dp[len(s)]

        # # memoization
        # wordSet = set(wordDict)
        # dp = [[-1]*(len(s)+1) for _ in range(len(s)+1)]

        # def f(start,end):
        #     if end == len(s) - 1:
        #         if s[start:end+1] in wordSet:
        #             return True
        #         return False
        #     if dp[start][end] != -1:
        #         return dp[start][end]
            
        #     take = False
        #     if s[start:end+1] in wordSet:
        #         take = f(end+1,end+1)

        #     extend = f(start,end+1)
        #     dp[start][end] = take or extend
        #     return dp[start][end]
        
        # return f(0,0)

        # recursion
        # wordSet = set(wordDict)
        # def f(start,end):
        #     if end == len(s) - 1:
        #         if s[start:end+1] in wordSet:
        #             return True
        #         return False
                 
        #     if s[start:end+1] in wordSet:
        #         return f(end+1,end+1)
        #     return f(start,end+1)
        
        # return f(0,0)
        