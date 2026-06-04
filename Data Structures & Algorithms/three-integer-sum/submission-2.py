# brute force
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         l = len(nums)
#         res = set()
#         for i in range(l):
#             for j in range(i+1,l):
#                 for k in range(j+1,l):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         res.add(tuple([nums[i],nums[j],nums[k]]))
#         return [list(i) for i in res]

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
                    # need to reduce the three sum hence need to check for a smaller element
                    k -=1
                elif threeSum < 0:
                    # need to increase the sum hence increase the element
                    j +=1
                else:
                    res.append([x,nums[j],nums[k]])
                    j +=1
                    k -=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res

        # for i in range(l):

        #     target = -nums[i]
        #     print(f"target: {target}")
        #     j, k = i, l-1
        #     while j < k:
        #         # -x = y+z
        #         x,y = nums[j], nums[k]
        #         print(x+y)
        #         sum = x +y
        #         if sum < target:
        #             j +=1
        #         elif sum > target:
        #             k -=1
        #         elif sum==target:
        #             res.append([nums[i],x,y])
        #             j +=1
        #             k -=1
        # return res                
                

# x + y + z = 0
# x + y = -z
# x=l; y=r;
# check for occurence of -z 
# for each element i, check for two other elements whose sum is -x
# x = -y -z
        