# brute force
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

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        prefix[0] = postfix[n - 1] = 1

        
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]

        for j in range(n-2, -1, -1):
            postfix[j] = nums[j+1] * postfix[j+1]

        print(prefix)
        print(postfix)
        # res[i] = prefix[i] * postfix[i]
        result = [0] * n
        for i in range(n):
            result[i] = prefix[i] * postfix[i]
        return result



            

