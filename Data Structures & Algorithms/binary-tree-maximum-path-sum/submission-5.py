# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        output = float('-inf')
            
        def dfs(cur):    
            if not cur:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            highest = max(cur.val, cur.val + left, cur.val + right)
            nonlocal output
            output = max(output, highest, cur.val + left + right)

            return highest
        
        dfs(root)

        return output
