class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.max_non_adjacent_sum(nums[1:]), self.max_non_adjacent_sum(nums[:-1]))
    
    def max_non_adjacent_sum(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            cur_loot = max(rob2, rob1 + num)
            rob1 = rob2
            rob2 = cur_loot
        return rob2