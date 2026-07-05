class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        each index, break into word from dict and recursively process remaining string 
        dimensions idx, str

        '''
        dp = [False]*(len(s)+1)

        dp[len(s)] = True

        for i in range(len(s) -1 ,-1,-1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

        # =======
        # dp = [[-1]*(len(s) + 1) for _ in range(len(s)+1)]
        # def f(start,end):
        #     if end == len(s) - 1:
        #         if s[start:end+1] in wordDict:
        #             return True
        #         return False            
        #     if dp[start][end] != -1:
        #         return dp[start][end]

        #     take = False
        #     if s[start:end+1] in wordDict:
        #         take = f(end+1,end+1)
        #     extend = f(start,end+1)
        #     dp[start][end] = take or extend
        #     return dp[start][end]
        # return f(0,0)
