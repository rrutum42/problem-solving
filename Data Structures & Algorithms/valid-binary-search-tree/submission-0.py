# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.valid(root, float("-inf"), float("inf"))
    
    def valid(self, node: Optional[TreeNode], lower: float, upper: float) -> bool:
        if not node:
            return True
        if not (lower < node.val < upper):
            return False
        
        return self.valid(node.left, lower, node.val) and self.valid(node.right, node.val, upper)
'''
WRONG: WE need to check the value of the node wrt to the root value as well
for each node check if left< node and node<right 
if not then return false
if yes then check for the left and right subtree
'''        
         
        