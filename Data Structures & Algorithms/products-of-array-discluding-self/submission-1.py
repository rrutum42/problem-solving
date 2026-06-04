# brute force
# time O(n^2)
# space O(1) and O(n) for output array
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [[] for x in range(len(nums))]
#         for i in range(len(nums)):
#             mul = 1
#             for j in range(len(nums)):
#                 if i != j:
#                    mul *= nums[j]
#             res[i] = mul
#         return res 

# nums[i] = nums[i+1] * nums[i+2] * ... * nums[len]

# sub optimal 
# time and space = O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix = [0] * n
#         postfix = [0] * n
#         prefix[0] = postfix[n - 1] = 1

        
#         for i in range(1,n):
#             prefix[i] = nums[i-1] * prefix[i-1]

#         for j in range(n-2, -1, -1):
#             postfix[j] = nums[j+1] * postfix[j+1]

#         print(prefix)
#         print(postfix)
#         # res[i] = prefix[i] * postfix[i]
#         result = [0] * n
#         for i in range(n):
#             result[i] = prefix[i] * postfix[i]
#         return result

#optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = prefix =1
        for i in range(n):
            # fill prefix on the next block
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1,-1,-1):
            # fill the postfix in the previous block
            res[i] *= postfix
            postfix *= nums[i]
        return res
            

# i = 3; postfix=1; res[3]=6*1=6;
# i = 2; postfix=1*4=4; res[2]=4*2=8
# i = 1; postfix=4*3=12; res[1]=