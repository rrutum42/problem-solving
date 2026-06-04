class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""   
        if s == t:
            return s 

        freq, window = {}, {}
        for char in t:
            freq[char] = freq.get(char,0) + 1
        needs = len(freq)

        have = 0
        min_ln = float("infinity")
        res = [-1,-1]
        l=r=0
        for r in range(len(s)): 
            ch = s[r]

            window[ch] = window.get(ch,0) + 1

            if ch in freq and window[ch] == freq[ch]:
                have +=1

            while have == needs:
                if (r-l+1) < min_ln:
                    res= [l,r]
                    min_ln = r-l+1

                window[s[l]] -= 1
                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -=1
                l+=1
        l, r = res
        
        return s[l: r+1] if min_ln != 0 else ""
'''
EXPAND FROM RIGHT AND MINIMISE FROM LEFT. DONT GO CHECKING FOR THE ENTIRE STRING FOR EACH L (BASICALLY NO R=L)
MAINTAIN NEEDS AND HAVE
First move the right pointer till have = need
Then remove from left till have != need 
then move the right pointer till have = need 
...
'''

# brute force
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         ans = ""
#         if len(s)<len(t):
#             return ans   
#         if s == t:
#             return s 

#         freq = {}
#         # O(t)
#         # O(len(t))
#         for char in t:
#             freq[char] = freq.get(char,0) + 1
        
#         l=0
#         while l<len(s): # l < 13-3=10
#             cpy = freq.copy()
#             if freq.get(s[l],None): # A|D|O|B|E|C
#                 subs = ""
#                 r = l # 0|3|5
#                 while len(cpy)>0: # 3,2,2,1,1,0 | 3,2,1,0| 3,2,2,2,1
#                     if cpy.get(s[r],None): #A,D,O,B,E,C | B,E,C,O,D,E,B,A | C,O,D,E,B,A
#                         if cpy[s[r]] == 1:
#                             del cpy[s[r]] # b,c;c;empty|a,c;a;empty|a,b;a;empty
#                         else:
#                             cpy[s[r]] -= 1
#                     subs += s[r]  # A,AD,ADO,ADOB,ADOBE,ADOBEC| B,BE,BEC,BECO,BECOD,BECODE,BECODEB,BECODEBA
#                     # C,CO,COD,CODE,CODEB,CODEBA
#                     r +=1 # 1,2,3,4,5,6|4,5,6,7,8,9,10,11|6,7,8,9,10,11
#                     if r == len(s):
#                         break
#                 # print(subs)  # ADOBEC      
#                 if len(cpy) == 0:
#                     if ans == "": # ""|"ADOBEC"
#                         ans = subs # ADOBEC
#                     elif len(subs)<len(ans): #8<6
#                         ans = subs

#             l +=1 # 1,2,3,4,5

#         return ans
'''
window size is atleast len(t)
hashmap to count occurences of chars in t 
for each char in the window, 
for l if l not in 

s= apqstbcza , t = abc
ans = 4 -> (bcza)

window 1 
apqstbcza - include all chars till t is not empty 

keep shifting left ptr till a element is encountered which is in t

window 2
bcza
---
adobecodebanc abc

adobec,becodeba,codeba,banc 
---
axyazbc abc
axyazbc, azbc
'''