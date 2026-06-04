class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l, r = 0, n-1
        while l<r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l+1,r+1]
            elif sum > target:
                r -= 1
            elif sum < target:
                l += 1
    
# O(n), O(1)
