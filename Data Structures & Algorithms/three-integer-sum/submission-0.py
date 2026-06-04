class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums = sorted(nums)
        res = []

        for i,x in enumerate(nums):
            if x>0:
                break
            if i>0 and x == nums[i-1]:
                # don't check for the same number again
                continue

            j,k = i+1, l-1

            while j<k:
                threeSum = x + nums[j] + nums[k]
                # print(f"x {x}, y {nums[j]}, z {nums[k]}, threeSum {threeSum}")
                if threeSum > 0:
                    k -=1
                elif threeSum < 0:
                    j +=1
                else:
                    res.append([x,nums[j],nums[k]])
                    j +=1
                    k -=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res