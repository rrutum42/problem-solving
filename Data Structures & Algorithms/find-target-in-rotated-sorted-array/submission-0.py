class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is O(n) so can't do    
        # if target not in nums:
        #     return -1 

        ln = len(nums)
        l,r = 0, ln - 1

        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        res = l

        # print(f"pivot: {res}")
        # [4,5,0,1,2,3]
        result = self.binarySearch(nums,target,0, res-1)
        if result != -1:
            return result
        return self.binarySearch(nums,target, res, ln-1)
        # choose right segment [0,1,2,3]
        # if nums[res] <= target:
        #     # l,r = res,ln
        #     return self.binarySearch(nums,target, res, ln)
        # #choose left segment [4,5]
        # elif target <= nums[res-1]:
        #     return self.binarySearch(nums,target, 0, res-1)
    
    def binarySearch(self, nums: List[int], target: int, l: int, r: int) -> int:
        # l,r = 0, res-1
        while l<=r:

            m = (l+r)//2
            # print(f"l {l} r {r} m {m}")
            if nums[m] == target:
                return m
            elif nums[m]<target:
                l = m + 1
            else:
                r = m - 1
        return -1
        # while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     return -1

'''
[3,4,0,1,2]
 l.  m.  r. res = 0
l,m r       res = 0
'''

'''
target = 1 -> 
[4,5,0,1,2,3]
 l.  m     r 

[0,1,2,3,4,5]
 l.  m.    r
if m ==target :
    return m
if m < target:
    if l<target:
        move left
    elif l == target:
        return l
    elif l>target:
        move right
elif m > target:


target = 0 -> 
[4,5,6,7,0,1,2,3]
 l.    m       r 

[0,1,2,3,4,5,6,7]
 l.    m.      r
'''