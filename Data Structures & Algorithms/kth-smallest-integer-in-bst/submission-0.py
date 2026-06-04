# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative
        '''
        pop node in stk if it has left element. Go to the left.
        If node.left is not present then pop the node from stack and 
        move to the right child
        '''
        stk = []
        cur = root

        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            
            cur = stk.pop()
            k-=1
            if k == 0:
                return cur.val
            cur=cur.right

        # recursive: O(n), O(n)
        # arr = []
    
        # def dfs(root: Optional[TreeNode]):
        #     if not root:
        #         return 
            
        #     dfs(root.left)
        #     arr.append(root.val)
        #     dfs(root.right)
        
        # dfs(root)
        # return arr[k-1]
        