class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        prefix, suffix = 0,0
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-1-i]

            ans = max(ans,max(prefix,suffix))
        
        return ans
'''
cases:
1. If all positive then product of all
2. If even num of negative then product of all
3. If odd num of negatives then product of prefix or product of suffix
4. If 0 is in middle, reset the product to 1 and find product of the subarray after 0
'''
        