from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        binary search
        1. Maintain multiple arrays. Each array is a LIS.
        2. For each element check if it can be appended to each subarray(if it is greater than the last element), if yes append it to the end. If no then create a new array with all elements smaller than it that we have previously seen.
        3. The length of the maximum of these arrays is the LIS
        Space optimised:
        1. Maintain a single array
        2. For each element insert the element at the end if no element is bigger than it OR 
           if element is already present in the array replace it OR
           if element is not present in array, replace it with the lowest number higher than element
        3. Length of this array is the ans
        Use binary search
        '''
        n = len(nums)

        arr = []
        # since the first element will never have a previous one
        arr.append(nums[0])
        for i in range(1,n):
            # if bigger than the last elemnt then append
            if nums[i] > arr[-1]:
                arr.append(nums[i])
            else:
                idx = bisect_left(arr, nums[i])
                arr[idx] = nums[i]
        return len(arr)

        # tabulation space optmised O(n^2), O(n)
        n = len(nums)
        # dp = [[0]*(n+1) for _ in range(n+1)]
        cur = [0 for _ in range(n+1)]
        next = [0 for _ in range(n+1)]

        # base case is 0
        # idx n-1 -> 0
        # prev idx-1 -> -1 
        for idx in range(n-1,-1,-1):
            for prev in range(idx-1,-2,-1):
                # if you don't take the idx moves and prev remains the same
                not_take = 0 + next[prev+1]
                # if you take then pick the max
                take = 0
                if (prev == -1 or nums[idx]>nums[prev]):
                    take = 1 + next[idx+1]
                cur[prev+1] = max(take, not_take)
            next = cur
        return cur[-1+1]

        # tabulation: O(n^2), O(n^2)
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]

        # base case is 0
        # idx n-1 -> 0
        # prev idx-1 -> -1 
        for idx in range(n-1,-1,-1):
            for prev in range(idx-1,-2,-1):
                # if you don't take the idx moves and prev remains the same
                not_take = 0 + dp[idx+1][prev+1]
                # if you take then pick the max
                take = 0
                if (prev == -1 or nums[idx]>nums[prev]):
                    take = 1 + dp[idx+1][idx+1]
                dp[idx][prev+1] = max(take, not_take)
        return dp[0][-1+1]

        # memoization: O(n^2), O(n^2)
        n = len(nums)
        
        # idx goes from 0 to n-1 -> n size
        # prev goes from -1 to n -1 -> m size
        # to accomodate the nXm array we need to coordinate change 
        dp = [[-1]*(n+1) for _ in range(n)]

        def f(idx, prev):
            if idx == n:
                return 0
            if dp[idx][prev] != -1:
                return dp[idx][prev]
            # if you don't take the idx moves and prev remains the same
            not_take = 0 + f(idx+1,prev)
            # if you take then pick the max
            take = 0
            if (prev == -1 or nums[idx]>nums[prev]):
                take = 1 + f(idx+1,idx)
            dp[idx][prev] = max(take, not_take)
            return dp[idx][prev]

        return f(0,-1)
        
        # # recursion O(2^n), O(n)
        # n = len(nums)

        # def f(idx, prev):
        #     if idx == n:
        #         return 0
            
        #     # if you don't take the idx moves and prev remains the same
        #     not_take = 0 + f(idx+1,prev)
        #     # if you take then pick the max
        #     take = 0
        #     if (prev == -1 or nums[idx]>nums[prev]):
        #         take = 1 + f(idx+1,idx)
        #     len = max(take, not_take)
        #     return len

        # return f(0,-1)    
'''
For subsequence you can either take or not take the element
'''            
        