class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]

        def dfs(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            if total > target or i>=len(nums):
                return
            
            # add the current element to curr list
            cur.append(nums[i])
            # include the number
            dfs(i,cur,total+nums[i])

            # don't include the number 
            cur.pop()
            dfs(i+1,cur,total)

            
        
        dfs(0,[],0)
        return res
'''
decision tree, at each level we consider all the nums in the list 
we dont proceeed further if
sum >= target

sum is the backtracking part
'''