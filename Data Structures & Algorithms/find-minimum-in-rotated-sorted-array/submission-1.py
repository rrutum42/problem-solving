class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
'''
[3,1,2]
 l   r. res=3
 l m r  res=1
l,r
'''        
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         ln = len(nums)
#         l , r = 0, ln - 1
#         while l<=r:
#             m = (l+r)//2
#             # already sorted without rotation
#             if nums[l]<= nums[m] and nums[m]<=nums[r]:
#                 return nums[l]
#             # we need to move to this side
#             if nums[m] < nums[l]:
#                 r = m - 1
#             elif nums[m] > nums[r]:
#                 l = m + 1
#             elif m==r or m==l:
#                 return nums[m] 

"""
[3,1,2]
 l m r
 l    
we need to find where the cut is for the given array (where arr[i]<arr[i-1])
l = 0 ; r = n-1; m = (l+r)//2
out of l,m,r two of them will be in the same segment
we need to move m to the other segment
if m > l:
    l = m
elif m < r:

[2,3,0,1]
l  m   r 
   l m r 
break when m<l and m<r
[0,1,2,3,4]
l    m   r

[4,0,1,2,3]
l    m   r

[2,0,1]
 l m r 
 l r
 m
   r
   m
if l<m<r:
    already sorted, pick the first element
else:
    if val l>m:
        go left
    elif val m>r:
        go right
    elif m<l and m<r:
        break
    if m==r==l:
        break
"""
        