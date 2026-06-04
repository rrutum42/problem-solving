class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2), O(n)
        start = 0 
        maxLen = 0

        def expand_around_centre(l,r):
            nonlocal start, maxLen
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    start = l
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand_around_centre(i,i)
            expand_around_centre(i,i+1)
        
        return s[start:start+maxLen]

        # O(n^2), O(n^2)
        # n = len(s)
        # dp = [[0]* n for _ in range(n)]

        # start = 0
        # maxLen = 1 

        # # mark diagonal as substring
        # for i in range(n):
        #     dp[i][i] = 1

        # # mark the next diagonal values:
        # for i in range(n-1):
        #     if s[i] == s[i+1]:
        #         dp[i][i+1] = 1
        #         if maxLen == 1:
        #             maxLen = 2
        #             start = i

        # # for i in range(n):
        # #     print(",".join(str(dp[i])))

        # # fill the next diagonals (0,2)->(1,3)->(2,4)->..(5,7)-> 0,3->1,4->2,5->..4,7 -> 

        # for length in range(3,n+1): #3,4,5,6,7
        #     for i in range(n - length + 1): # 0,1,2,3,4,5
        #         '''
        #         8-3+1 = 6
        #         '''
        #         j = i + length - 1 # 2,3,4,5,6
        #         # palindrome if previous and this letter are same and previous dp is 1
        #         if s[i] == s[j] and dp[i+1][j-1] == 1:
        #             dp[i][j] = 1
        #             if length > maxLen:
        #                 maxLen = length
        #                 start = i
        # # print(maxLen)
        # end = start+maxLen
        # return s[start:end]

        
        
