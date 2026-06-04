class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        sett = set()
        ls=0
        while r<len(s):
            if s[r] not in sett:
                sett.add(s[r])
                r +=1
                ls = max(ls,len(sett))
            else:
                sett.remove(s[l])
                l += 1
        return ls

'''
dynamic sliding window

l=0,
l=r
if r not in set:
    add r to set 
    r++
else if r is in set:
    remove l from set and then l++, r++


'''

        