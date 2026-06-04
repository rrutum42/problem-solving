class Solution:
    def rob(self, nums: List[int]) -> int:
        # tabulation
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = nums[0], max(nums[0],nums[1])
        for i in range(2,len(nums)):
            # either the last house robbery or the last - 1 robbery plus i house amount
            cur_loot = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = cur_loot
        return rob2

        # # memoization
        # idx = len(nums) - 1
        # dp = [-1]*(len(nums)+1)
        # def rob_house(idx):
        #     if idx == 0:
        #         return nums[0]
        #     if idx == 1:
        #         return max(nums[0],nums[1])
        #     if dp[idx] != -1: 
        #         return dp[idx]
        #     loot = rob_house(idx - 2) + nums[idx]
        #     dp[idx] = max(rob_house(idx-1), loot)
        #     return dp[idx]
        
        # return rob_house(idx)

        # # recursion 
        # idx = len(nums) - 1
        # def rob_house(idx):
        #     if idx == 0:
        #         return nums[0]
        #     if idx == 1:
        #         return max(nums[0],nums[1])
        #     loot = rob_house(idx - 2) + nums[idx]
        #     return max(rob_house(idx-1), loot)
        
        # return rob_house(idx)