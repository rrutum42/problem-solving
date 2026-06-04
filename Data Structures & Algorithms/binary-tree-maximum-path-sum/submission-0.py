# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # ignore the leftMax and rightMax if both are negative
            leftMax = max(leftMax,0) 
            rightMax = max(rightMax, 0)
            # update the result with max sum with splitting
            # max(result, node.val + node.left.val + node.right.val)
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # return the max sum without split
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
'''
Sum path for current node is
node.val + node.left.val + node.right.val

3 options to consider:
1. Consider only the left or right subtree
2. Consider both subtrees
3. Consider only this node

return value is the max sum without splitting
result is appending with the max sum with splitting
'''        