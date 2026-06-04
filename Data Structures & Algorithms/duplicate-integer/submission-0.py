class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
            if map[n] > 1:
                return True
        return False       