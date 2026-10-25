# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        output = 0
            
        def dfs(cur):    
            if not cur:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            nonlocal output
            output = max(output, left + right)

            return 1 + max(left, right)

        dfs(root)

        return output