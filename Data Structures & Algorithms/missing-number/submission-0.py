class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res += i
        for num in nums:
            res -= num
        return res
        '''
        We sum all the numbers till n and then subtract each nums from the result
        the remaining result is the missing number
        '''
        # n = len(nums)
        # xorr = n
        # for i in range(n):
        #     xorr ^= i ^ nums[i]
        # return xorr
'''
we iterate through the list
xor each number with the
'''
