class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in m:
                m[nums[i]] = i
            else:
                return [m[difference], i]
        
        # nums[i] == target - nums[j]
# nums = [4,5,6], target = 10
# i=0 difference=6 m={4:0}
# i=1 diff=5 m={4:0,5:1}
# i=2 diff=4 m={4:0,5:1} --> return 0,2
        