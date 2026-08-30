'''
TC O(logn)
SC O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        while l < r:
            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        pivot = l

        leftSrch = self.binarySearch(nums,target,0,pivot-1)
        if leftSrch != -1:
            return leftSrch
        
        return self.binarySearch(nums,target,pivot,len(nums)-1)
    
    def binarySearch(self, nums, target, l, r):
        while l<= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


    