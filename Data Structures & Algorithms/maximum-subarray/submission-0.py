class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TC O(n), SC O(1)
        n = len(nums)
        sum = 0
        maxs = nums[0]
        start,end = 0,0
        for i,num in enumerate(nums):
            # we don't want to carry forward a negative sum, so we reset it to 0
            if sum < 0:
                sum = 0
                start = i
            # add the element to the sum
            sum += num
            # if the current sum is max then maxs then update maxs
            if sum > maxs:
                end = i
                maxs = sum
            
            # maxs = max(maxs,sum)
        # print the subarray
        # print(nums[start:end+1])
        return maxs

        # n = len(nums)
        # sum = -1e6
        # maxs = float('-inf')
        # def f(idx, pick):
        #     if idx == len(n):
        #         return 0 if pick else -1e6
        #     if pick:
        #         return max(0, nums[idx] + f(i+1, True))
        #     return max()
            
'''
If all positive, sum will be sum of all
If even 1 negative, need to find which one is max subarray
naive:
for each index, check the sum of all the subarrays by moving right index. 
update a max element along the way. 
O(n^2)

recursion -> consider the next element or dont consider it

'''
        