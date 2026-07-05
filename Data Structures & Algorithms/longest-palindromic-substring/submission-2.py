class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        as curr str as centre calc len of palindrome
        '''
        start = 0
        maxLen = 0

        def expand_around_centre(l,r):
            nonlocal start,maxLen
            while l>=0 and r<len(s) and s[l] == s[r]:
                currLen =  r - l + 1
                if currLen > maxLen:
                    maxLen = currLen
                    start = l
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd
            expand_around_centre(i,i)
            # even
            expand_around_centre(i,i+1)

        return s[start:start+maxLen]