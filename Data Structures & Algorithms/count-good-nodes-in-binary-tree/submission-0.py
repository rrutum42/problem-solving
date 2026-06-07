# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root is always good
        self.count = 0

        def dfs(node, maxSoFar):
            if not node:
                return 0
            if node.val >= maxSoFar:
                self.count += 1
                maxSoFar = max(maxSoFar, node.val)
            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)

        dfs(root, root.val)
        return self.count
