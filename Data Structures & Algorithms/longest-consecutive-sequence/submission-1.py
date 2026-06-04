# brute force
# time O(nlogn)
# space O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums = sorted(list(set(nums)))
#         lcs = 1
#         l = 1
#         for i in range(len(nums)-1):
#             if nums[i+1] - nums[i] == 1:
#                 l += 1
#                 lcs = max(lcs,l)
#             else:
#                 lcs = max(lcs,l)
#                 l = 1
#         return lcs

# sort the array, make a set
# for every element check if the the next element = curr + 1
# if yes: increase the length 
# if no: reset the counter to 0 and set lcs = max(lcs,length)
# keep looping

#optimal 
# 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums) # O(n)
        lcs = 1 
        for x in nums: # O(n)
            if x-1 not in s: # only expand for elements whose -1 doesn't exist in array
                y = x
                l = 0
                while y in s:
                    l += 1
                    y +=1
                lcs = max(lcs,l)
        return lcs

'''
what if for every element x we check if nums[x+1] exists or not
existence is a O(n) operation
but this would make complexity O(n^2)

convert array to set
for every element x, check if x -1 exists in set.
if yes then check if x + 1, x + 2, ... x + n element exists or not
'''
        