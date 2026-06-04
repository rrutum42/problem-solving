class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        
        l=r=0
        ans = 0
        while r<len(s):
            c[s[r]] = c.get(s[r], 0) + 1
            # shrink until valid
            while (r - l + 1) - self.freqMaxOccuringChar(c) > k:
                c[s[l]] -= 1
                l += 1
            ans = max(ans,(r-l+1))
            r = r+1
        return ans

    def freqMaxOccuringChar(self, c: dict) -> int:
        maxc = 0
        # for i in range(len(c)):
        for key, val in c.items():    
            maxc = max(maxc, val)  
        return maxc
'''
for every r increase the count of r in hashmap
check if r-l - max_occuring_char_cnt <= k 
ans = max(ans,(l-r+1))
then more r to right
else
reduce the count of l from map by 1 
move l to right
'''


         