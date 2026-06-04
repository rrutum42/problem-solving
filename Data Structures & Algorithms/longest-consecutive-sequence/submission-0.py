class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        lcs = 1
        l = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                l += 1
                lcs = max(lcs,l)
            else:
                lcs = max(lcs,l)
                l = 1
        return lcs

# sort the array, make a set
# for every element check if the the next element = curr + 1
# if yes: increase the length 
# if no: reset the counter to 0 and set lcs = max(lcs,length)
# keep looping


        