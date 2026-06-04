class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxj = 0
        for i,num in enumerate(nums):
            if i > maxj:
                return False
            maxj = max(i+num,maxj)
    
            if maxj >= len(nums) - 1:
                return True